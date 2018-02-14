# -*- coding: utf-8 -*-
import requests,shutil,random,string,json,os,tempfile
import unicodedata
from Api import Poll, Talk, channel
from random import randint
from time import time
from datetime import datetime
from lib.curve.ttypes import *

def def_callback(str):
    print(str)

class LINE:

  mid = None
  authToken = None
  cert = None
  channel_access_token = None
  token = None
  obs_token = None
  refresh_token = None


  def __init__(self):
    self.Talk = Talk()
    self._session = requests.session()
    self._headers = {'X-Line-Application': 'IOSIPAD\t7.18.0\tiPhone OS\t11.12.1', 'X-Line-Access': self.authToken, 'User-Agent': 'Line/8.0.0 iPad4,1 9.0.2'}

  def login(self, mail=None, passwd=None, cert=None, token=None, qr=False, callback=None):
    if callback is None:
      callback = def_callback
    resp = self.__validate(mail,passwd,cert,token,qr)
    if resp == 1:
      self.Talk.login(mail, passwd, callback=callback)
    elif resp == 2:
      self.Talk.login(mail,passwd,cert, callback=callback)
    elif resp == 3:
      self.Talk.TokenLogin(token)
    elif resp == 4:
      self.Talk.qrLogin(callback)
    else:
      raise Exception("invalid arguments")

    self.authToken = self.Talk.authToken
    self.cert = self.Talk.cert
    self._headers = {
              'X-Line-Application': 'IOSIPAD\t7.18.0\tiPhone OS\t11.12.1',
              'X-Line-Access': self.authToken,
              'User-Agent': 'Line/8.0.0'
   }

    self.Poll = Poll(self.authToken)
    self.channel = channel.Channel(self.authToken)
    self.channel.login()

    self.mid = self.channel.mid
    self.channel_access_token = self.channel.channel_access_token
    self.token = self.channel.token
    self.obs_token = self.channel.obs_token
    self.refresh_token = self.channel.refresh_token

  """User"""

  def getProfile(self):
    return self.Talk.client.getProfile()

  def getSettings(self):
    return self.Talk.client.getSettings()

  def getUserTicket(self):
    return self.Talk.client.getUserTicket()

  def updateProfile(self, profileObject):
    return self.Talk.client.updateProfile(0, profileObject)

  def updateSettings(self, settingObject):
    return self.Talk.client.updateSettings(0, settingObject)

  def CloneContactProfile(self, mid):
    contact = self.getContact(mid)
    profile = self.getProfile()
    profile.displayName = contact.displayName
    profile.statusMessage = contact.statusMessage
    profile.pictureStatus = contact.pictureStatus
    self.updateDisplayPicture(profile.pictureStatus)
    return self.updateProfile(profile)

  def updateDisplayPicture(self, hash_id):
    return self.Talk.client.updateProfileAttribute(0, 8, hash_id)

    """File"""

  def deleteFile(self, path):
        if os.path.exists(path):
            os.remove(path)
            return True
        else:
            return False

  def downloadFileURL(self, fileUrl, returnAs='path', saveAs=''):
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        if saveAs == '':
            saveAs = self.genTempFile()
        r = self.server.getContent(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download file failure.')

  def genTempFile(self, returnAs='path'):
        try:
            if returnAs not in ['file','path']:
                raise Exception('Invalid returnAs value')
            fName, fPath = 'linepy-%s-%i.bin' % (int(time.time()), randint(0, 9)), tempfile.gettempdir()
            if returnAs == 'file':
                return fName
            elif returnAs == 'path':
                return '%s/%s' % (fPath, fName)
        except:
            raise Exception('tempfile is required')

  def genOBSParams(self, newList, returnAs='json'):
        oldList = {'name': self.genTempFile('file'),'ver': '1.0'}
        if returnAs not in ['json','b64','default']:
            raise Exception('Invalid parameter returnAs')
        oldList.update(newList)
        if 'range' in oldList:
            new_range='bytes 0-%s\/%s' % ( str(oldList['range']-1), str(oldList['range']) )
            oldList.update({'range': new_range})
        if returnAs == 'json':
            oldList=json.dumps(oldList)
            return oldList
        elif returnAs == 'b64':
            oldList=json.dumps(oldList)
            return base64.b64encode(oldList.encode('utf-8'))
        elif returnAs == 'default':
            return oldList


  """Personalize"""

  def updateProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if type == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True

  def updateProfileVideoPicture(self, path):
        try:
            from ffmpy import FFmpeg
            files = {'file': open(path, 'rb')}
            data = {'params': self.genOBSParams({'oid': self.profile.mid,'ver': '2.0','type': 'video','cat': 'vp.mp4'})}
            r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn', data=data, files=files)
            if r_vp.status_code != 201:
                raise Exception('Update profile video picture failure.')
            path_p = self.genTempFile('path')
            ff = FFmpeg(inputs={'%s' % path: None}, outputs={'%s' % path_p: ['-ss', '00:00:2', '-vframes', '1']})
            ff.run()
            self.updateProfilePicture(path_p, 'vp')
        except:
            raise Exception('You should install FFmpeg and ffmpy from pypi')

  """Object"""

  def downloadObjectMsg(self, messageId, returnAs='path', saveAs=''):
        if saveAs == '':
            saveAs = self.genTempFile('path')
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        params = {'oid': messageId}
        url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/talk/m/download.nhn', params)
        r = self.server.getContent(url)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download object failure.')

  def forwardObjectMsg(self, to, msgId, contentType='image'):
        if contentType not in ['image','video','audio']:
            raise Exception('Type not valid.')
        data = self.genOBSParams({'oid': 'reqseq','reqseq': self.revision,'type': contentType,'copyFrom': '/talk/m/%s' % msgId},'default')
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/copy.nhn', data=data)
        if r.status_code != 200:
            raise Exception('Forward object failure.')
        return True


  """Operation"""

  def fetchOperation(self, revision, count):
        return self.Poll.client.fetchOperations(revision, count)

  def fetchOps(self, rev, count):
        return self.Poll.client.fetchOps(rev, count, 0, 0)

  def getLastOpRevision(self):
        return self.Talk.client.getLastOpRevision()

  def stream(self):
        return self.Poll.stream()

  def downloadFileURL(self, fileUrl, returnAs='path', saveAs=''):
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        if saveAs == '':
            saveAs = self.genTempFileName()
        r = self.server.getContent(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download file failure.')

  
  """Message"""

  def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

  def removeAllMessages(self, lastMessageId):
	return self.Talk.client.removeAllMessages(0,lastMessageId)

  def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)

  def kedapkedip(self, tomid, text):
        M = Message()
        M.to = tomid
        t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
        t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
        rst = t1 + text + t2
        M.text = rst.replace("\n", " ")
        return self.Talk.client.sendMessage(0, M)

  def zalgo(self, tomid, text):
        M = Message()
        M.to = tomid
        du = [' Ì',' Ì',' Ì',' Ì',' Ì¿',' Ì',' Ì',' Ì',' Í',' Í',' Í',' Ì',' Ì',' Ì',' Í',' Í',' Í',' Í',' Í',' Í',' Ì',' Ì',' Ì',' Í',' Ì',' Ì',' Ì',' Ì½',' Ì',' Í£',' Í¤',' Í¥',' Í¦',' Í§',' Í¨',' Í©',' Íª',' Í«',' Í¬',' Í­',' Í®',' Í¯',' Ì¾',' Í',' Í',' Ì',]
        dm = [' Ì',' Ì',' Í',' Í',' Í',' Ì¡',' Ì¢',' Ì§',' Ì¨',' Ì´',' Ìµ',' Ì¶',' Í',' Í',' Í',' Í',' Í ',' Í¢',' Ì¸',' Ì·',' Í¡',]
        rst = du + text + dm
        M.text = rst.replace("\n", " ")
        return self.Talk.client.sendMessage(0, M)

  def post_content(self, url, data=None, files=None):
        return self._session.post(url, headers=self._headers, data=data, files=files)

  def sendImage(self, to_, path):
        M = Message(to=to_, text=None, contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)            
        }       

        r = self.post_content('http://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        #print r
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True

  def sendImageWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download image failure.')
        try:
            self.sendImage(to_, path)
        except Exception as e:
            raise e

  def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('http://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
	print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

  def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

  def sendVideo(self, to_, path):
      M = Message(to=to_,contentType = 2)
      M.contentMetadata = {
           'VIDLEN' : '0',
           'DURATION' : '0'
       }
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'video',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True
      
  def sendVideoWithUrl(self, to_, url):
      path = 'pythonLines.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendVideo(to_, path)
      except Exception as e:
         raise e


  def sendEvent(self, messageObject):
        return self._client.sendEvent(0, messageObject)

  def sendChatChecked(self, mid, lastMessageId):
        return self.Talk.client.sendChatChecked(0, mid, lastMessageId)

  def getMessageBoxCompactWrapUp(self, mid):
        return self.Talk.client.getMessageBoxCompactWrapUp(mid)

  def getMessageBoxCompactWrapUpList(self, start, messageBox):
        return self.Talk.client.getMessageBoxCompactWrapUpList(start, messageBox)

  def getRecentMessages(self, messageBox, count):
        return self.Talk.client.getRecentMessages(messageBox.id, count)

  def getMessageBox(self, channelId, messageboxId, lastMessagesCount):
        return self.Talk.client.getMessageBox(channelId, messageboxId, lastMessagesCount)

  def getMessageBoxList(self, channelId, lastMessagesCount):
        return self.Talk.client.getMessageBoxList(channelId, lastMessagesCount)

  def getMessageBoxListByStatus(self, channelId, lastMessagesCount, status):
        return self.Talk.client.getMessageBoxListByStatus(channelId, lastMessagesCount, status)

  def getMessageBoxWrapUp(self, mid):
        return self.Talk.client.getMessageBoxWrapUp(mid)

  def getMessageBoxWrapUpList(self, start, messageBoxCount):
        return self.Talk.client.getMessageBoxWrapUpList(start, messageBoxCount)

  """Contact"""


  def blockContact(self, mid):
        return self.Talk.client.blockContact(0, mid)


  def unblockContact(self, mid):
        return self.Talk.client.unblockContact(0, mid)


  def findAndAddContactsByMid(self, mid):
        return self.Talk.client.findAndAddContactsByMid(0, mid)


  def findAndAddContactsByMids(self, midlist):
        for i in midlist:
            self.Talk.client.findAndAddContactsByMid(0, i)

  def findAndAddContactsByUserid(self, userid):
        return self.Talk.client.findAndAddContactsByUserid(0, userid)

  def findContactsByUserid(self, userid):
        return self.Talk.client.findContactByUserid(userid)

  def findContactByTicket(self, ticketId):
        return self.Talk.client.findContactByUserTicket(ticketId)

  def getAllContactIds(self):
        return self.Talk.client.getAllContactIds()

  def getBlockedContactIds(self):
        return self.Talk.client.getBlockedContactIds()

  def getContact(self, mid):
        return self.Talk.client.getContact(mid)

  def getContacts(self, midlist):
        return self.Talk.client.getContacts(midlist)

  def getFavoriteMids(self):
        return self.Talk.client.getFavoriteMids()

  def getHiddenContactMids(self):
        return self.Talk.client.getHiddenContactMids()


  """Group"""

  def findGroupByTicket(self, ticketId):
        return self.Talk.client.findGroupByTicket(ticketId)

  def acceptGroupInvitation(self, groupId):
        return self.Talk.client.acceptGroupInvitation(0, groupId)

  def acceptGroupInvitationByTicket(self, groupId, ticketId):
        return self.Talk.client.acceptGroupInvitationByTicket(0, groupId, ticketId)

  def cancelGroupInvitation(self, groupId, contactIds):
        return self.Talk.client.cancelGroupInvitation(0, groupId, contactIds)

  def createGroup(self, name, midlist):
        return self.Talk.client.createGroup(0, name, midlist)

  def getGroup(self, groupId):
        return self.Talk.client.getGroup(groupId)

  def getGroups(self, groupIds):
        return self.Talk.client.getGroups(groupIds)

  def getGroupIdsInvited(self):
        return self.Talk.client.getGroupIdsInvited()

  def getGroupIdsJoined(self):
        return self.Talk.client.getGroupIdsJoined()

  def inviteIntoGroup(self, groupId, midlist):
        return self.Talk.client.inviteIntoGroup(0, groupId, midlist)

  def kickoutFromGroup(self, groupId, midlist):
        return self.Talk.client.kickoutFromGroup(0, groupId, midlist)

  def leaveGroup(self, groupId):
        return self.Talk.client.leaveGroup(0, groupId)

  def rejectGroupInvitation(self, groupId):
        return self.Talk.client.rejectGroupInvitation(0, groupId)

  def reissueGroupTicket(self, groupId):
        return self.Talk.client.reissueGroupTicket(groupId)

  def updateGroup(self, groupObject):
        return self.Talk.client.updateGroup(0, groupObject)
  def findGroupByTicket(self,ticketId):
        return self.Talk.client.findGroupByTicket(0,ticketId)

#  def acquireGroupCallRoute(self, groupId):
 #       return self.Talk.client.call.acquireGroupCallRoute(groupId)

  #def acquireGroupCallRoute(self, groupId):
#        return self.Talk.client.call.acquireGroupCallRoute(groupId)

#  def getGroupCall(self, ChatMid):
 #       return self.Talk.client.call.getGroupCall(ChatMid)

  #def inviteIntoGroupCall(self, chatId, contactIds=[]):
   #     return self.Talk.client.call.inviteIntoGroupCall(chatId, contactIds)

  def updateGroupPicture(self, groupId, path):
        files = {'file': open(path, 'rb')}
        data = {'params': self.genOBSParams({'oid': groupId,'type': 'image'})}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/g/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update group picture failure.')
        return True

  """Room"""

  def createRoom(self, midlist):
    return self.Talk.client.createRoom(0, midlist)

  def getRoom(self, roomId):
    return self.Talk.client.getRoom(roomId)

  def inviteIntoRoom(self, roomId, midlist):
    return self.Talk.client.inviteIntoRoom(0, roomId, midlist)

  def leaveRoom(self, roomId):
    return self.Talk.client.leaveRoom(0, roomId)

  """TIMELINE"""

  def new_post(self, text):
    return self.channel.new_post(text)

  def like(self, mid, postid, likeType=1001):
    return self.channel.like(mid, postid, likeType)

  def comment(self, mid, postid, text):
    return self.channel.comment(mid, postid, text)

  def activity(self, limit=20):
    return self.channel.activity(limit)

  def getAlbum(self, gid):

      return self.channel.getAlbum(gid)
  def changeAlbumName(self, gid, name, albumId):
      return self.channel.changeAlbumName(gid, name, albumId)

  def deleteAlbum(self, gid, albumId):
      return self.channel.deleteAlbum(gid,albumId)

  def getNote(self,gid, commentLimit, likeLimit):
      return self.channel.getNote(gid, commentLimit, likeLimit)

  def getDetail(self,mid):
      return self.channel.getDetail(mid)

  def getHome(self,mid):
      return self.channel.getHome(mid)

  def createAlbum(self, gid, name):
      return self.channel.createAlbum(gid,name)

  def createAlbum2(self, gid, name, path):
      return self.channel.createAlbum(gid, name, path, oid)

  def __validate(self, mail, passwd, cert, token, qr):
    if mail is not None and passwd is not None and cert is None:
      return 1
    elif mail is not None and passwd is not None and cert is not None:
      return 2
    elif token is not None:
      return 3
    elif qr is True:
      return 4
    else:
      return 5

  def loginResult(self, callback=None):
    if callback is None:
      callback = def_callback

      prof = self.getProfile()

      print("TYPE PRANKBOTS")
      print("MID= " + prof.mid)
      print("NAMA= " + prof.displayName)
      print("TOKET= " + self.authToken)
      print("MENCRET= " + self.cert if self.cert is not None else "")
      print("CREATOR BY:ACIL")
#-========-----------------

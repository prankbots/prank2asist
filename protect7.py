# -*- coding: utf-8 -*-

import PRANKBOTS
from PRANKBOTS.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from gtts import gTTS
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, tempfile, glob, shutil, unicodedata, goslate


PB = PRANKBOTS.LINE()
PB.login(token="En45TVT2cueFZFQ03s28.jbCYKqV9J5TlIAYrqu8bIa.hgJVpGzPeESl5kMsfMlQR3FWqgMT2DwGstZjasfjEQU=")
PB.loginResult()
#ki11
PB1 = PRANKBOTS.LINE()
PB1.login(token="EnKCkKvDsEh0F6pW5bad.Wvu+dMkG395XOOdtVRCjdq.uPCGCj+VZnr2qUB5sGOG9Vm9Cot75G0qZ8g5pJ2KQJI=")
PB1.loginResult()
#INI AKUN KICKER YANG DI LUAR, FUNGSINYA UNTUK BACKUP
#JIKA AKUN UTAMA DI KICK MAKA DIA AKAN MASUK LALU KICK KELUAR LAGI
kl = PRANKBOTS.LINE()
kl.login(token="En1oTTUdLDncvCU64Zf3.4xqN84T1S5cNUGFR9jI9mW.CLSvaG0zB4S0DhvOsoX9YmYWjslT+irMJ5CQBcTz99g=")
kl.loginResult()

print "Tamii Bot"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage= """℘ґ∂ηк | в❍тѕ
『B༘̈́̈́L༘̈́̈́Ä༘́̈́C༘̈́̈́K༘̈́̈́   ̈́Ö༘́̈́F༘̈́̈́ ̈́  G༘̈́̈́Ä༘́̈́M༘̈́̈́Ë༘́̈́R༘̈́̈́』
_____________
🕯️ STYLE OF BOTS 🕯️
✰ Bot1 rename:[text]
✰ Bot2 rename:[text]
✰ Bot3 rename:[text]
✰ Bot4 rename:[text]
✰ Bot5 rename:[text]
✰ Bot6 rename:[text]
✰ All rename:[text]
✰ Allbio:[text]
✰ Bot1 clone @[name]
✰ Bot2 clone @[name]
✰ Bot3 clone @[name]
✰ Bot4 clone @[name]
✰ Bot5 clone @[name]
✰ Bot6 clone @[name]
✰ Comment:[text]
✰ Message:[text]
✰ gift1-18
✰ Spam gift
✰ Bot1-6 backup run
✰ Bot1-6 backup
✰ Group name:[text]
✰ Bot2   @bye
✰ Bot3   @bye
✰ Bot4   @bye
✰ Bot5   @bye
✰ Bot6   @bye
✰ Prank   @bye
✰ Center @bye
✰ Bye allgroups[own]
✰ Turn off bots
🕯️TRANSFER🕯️
✰ Admin on @[name]
✰ Expel on @[name]
✰ Expelall
🕯️INFO MEMBER🕯️
✰ Steal name    @[name]
✰ Steal Bio     @[name]
✰ Steal status  @[name]
✰ Steal mid     @[name]
✰ Steal contact @[name]
✰ Steal cover   @[name]
✰ Steal pict    @[name]
✰ Steal group pict
✰ Midpict:[mid]
🕯️BLOCKER 🕯️
✰ Ban    @[name]
✰ Unban  @[name]
✰ Banned[send contact]
✰ Unbanned[send contact]
✰ Ban repeat @[name]
✰ Clear banlist
✰ Mimic target @[name]
✰ Mimic untarget @[name]
✰ Add friend @[name]
🕯️ INVITATION 🕯️
✰ Invite:[mid]
✰ Invite user[contact]
✰ Invite me
✰  Prank in
🕯️ BOT SETTINGS 🕯️
✰ Auto join:on/off
✰ Auto leave:on/off
✰ Auto like:on/off
✰ Welcome message:on/off
✰ Auto notice:on/off
✰ Blockinvite:on/off
✰ Auto blockqr:on/off
✰ Namelock:on/off
✰ Mimic:on/off
✰ Auto add:on/off
✰ Check message
✰ Add message:[text]
✰ Comment:on/off
✰ Add comment:[text]
✰ Check comment
✰ Backup:on/off
✰ Gcancel:[number]
✰ Update welcome:[text]
✰ Check welcome message
🕯️ PROTECTION MODE🕯️
✰ Protect:low
✰ Protect:hight
✰ Rejectall
✰ Clean invites
✰ Clear invites
✰ Fuckyou
✰ Vkick @
✰ Nk [name]
✰ Kick:[mid]
✰ Purge
🕯️MODE SELFPRO🕯️
✰ Lurking
✰ Lurking result
✰ Link open
✰ Link close
✰ Gurl
✰ Remove chat
✰ Bot restart
✰ Group list
✰ Banlist
✰ Admin list
✰ Settings
✰ Ginfo
✰ Sticker [expression]
✰ Pranktag
✰ TL:[text]
✰ Mimic list
✰ Spamg[on/off][no][txt]
✰ Spam add:[text]
✰ Spam change:[text]
✰ Spam start:[number]
✰ Say [text]
✰ Me
✰ Speed
✰ Debug speed
✰ My mid
✰ Gcreator
✰ Halo
✰ Bot contact
✰ Bot mid
✰ Creator
✰ System
✰ Iconfig
✰ Kernel
✰ Cpu
✰ Responsename
✰ Help
✰ Mc:[mid]
🕯️BROWSER🕯️
✰ Lyric [][]
✰ Music [][]
✰ Wiki [text]
✰ Vidio [text]
✰ Youtube [text]
✰ Instagram [text]
✰ Emoji [expression]
✰ Info @[name]
✰ Ping
✰ Time
✰ apakah
🕯️BROADCASTING 🕯️
✰ Pm cast   [text]
✰ Broadcast [text]
✰ Spam @[name]
_____________
『B༘̈́̈́L༘̈́̈́Ä༘́̈́C༘̈́̈́K༘̈́̈́   ̈́Ö༘́̈́F༘̈́̈́ ̈́  G༘̈́̈́Ä༘́̈́M༘̈́̈́Ë༘́̈́R༘̈́̈́』
℘ґ∂ηк | в❍тѕ
 ____B_O_G____
"""
KAC=[PB,PB1,kl]
mid = PB.getProfile().mid
Emid = PB1.getProfile().mid
Fmid = kl.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid,Emid,Fmid,""]
admin = [""]
owner = [""]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"""❂•••••••••••••••••••••••••❂
                  https://line.me/R/ti/p/%40iya4481p
『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』
SUBCRABE YOUTUBE PRANK BOT:
https://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ""",
    "lang":"JP",
    "comment":"""❂•••••••••••••••••••••••••❂
                  https://line.me/R/ti/p/%40iya4481p
『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』
SUBCRABE YOUTUBE PRANK BOT:
https://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ""",
    "welmsg":"""❂•••••••••••••••••••••••••❂
SUBCRABE MY CHANNEL:: https://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ""",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "status":False,
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "welcomemsg":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}


setTime = {}
setTime = wait2['setTime']

contact = PB.getProfile()
backup = PB.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup = ks.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = PB1.getProfile()
backup = PB1.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       PB.sendMessage(msg)
    except Exception as error:
       print error
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
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
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = PB.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass

    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                PB.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    PB.sendText(op.param1,str(wait["message"]))


        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = PB.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = ks.getGroup(op.param1)
				    except:
					try:
                                            G = PB1.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        PB.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ks.updateGroup(G)
                                    except:
                                        try:
                                            PB1.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            PB1.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        kk.sendText(op.param1,"please do not change group name-_-")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        PB.sendMessage(c)

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        PB.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = PB1.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        PB1.updateGroup(X)
                        Ti = PB1.reissueGroupTicket(op.param1)
                        PB1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        PB1.updateGroup(X)
                        Ti = PB1.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in mid:
                        X = PB.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        PB.updateGroup(X)
                        Ti = PB.reissueGroupTicket(op.param1)
                        PB.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        PB.updateGroup(X)
                        Ti = PB.reissueGroupTicket(op.param1)
#=====================================================================================
                if op.param3 in mid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        PB.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        PB.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Dmid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        PB.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Emid:
                        X = PB1.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        PB1.updateGroup(X)
                        Ti = PB1.reissueGroupTicket(op.param1)
                        PB.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        PB1.updateGroup(X)
                        Ti = PB1.reissueGroupTicket(op.param1)
#======================================================
                if op.param3 in Bmid:
                    if op.param2 in mid:
                        G = PB.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        PB.updateGroup(G)
                        Ticket = PB.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        PB.updateGroup(G)
                        Ticket = PB.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        G = kc.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kc.updateGroup(G)
                        Ticket = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
                        Ticket = kc.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Dmid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Emid:
                        G = PB1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        PB1.updateGroup(G)
                        Ticket = PB1.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        PB1.updateGroup(G)
                        Ticket = PB1.reissueGroupTicket(op.param1)
#=========================================================================


#===========================================
        if op.type == 32:
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True:
                    try:
                        klist=[ki,kk,kc,ks,kt]
                        kicker = random.choice(klist)
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 13:
            if mid in op.param3:
                G = PB.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            PB.rejectGroupInvitation(op.param1)
                        else:
                            PB.acceptGroupInvitation(op.param1)
                    else:
                        PB.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        PB.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    PB.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                G = PB.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
            if Bmid in op.param3:
                G = PB.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)
            if Cmid in op.param3:
                G = PB.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kc.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("^^",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kc.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 17:
            if op.param3 in wait["blacklist"]:
                if not op.param2 in Bots and admin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    PB.sendText(op.param1,"blacklist users are not allowed to sign in  -_-")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param3}
                    PB.sendMessage(c)
        if op.type == 17:
	   if wait["welcomemsg"] == True:
              if op.param2 not in Bots:
                 ginfo = PB.getGroup(op.param1)
                 PB.sendText(op.param1,PB.getContact(op.param2).displayName + wait["welmsg"]+ str(ginfo.name))
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:
                try:
                    klist=[ki,kk,kc,ks,kt]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots and admin:
              if wait["protectionOn"] == True:
                 try:
                    klist=[ki,kk,kc,ks,kt]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    PB.sendText(op.param1,"please do not open link group-_-")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param2}
                    PB.sendMessage(c)

                 except Exception, e:
                           print e
        if op.type == 13:
            G = PB.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True:
                    klist=[ki,kk,kc,ks,kt]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        PB.sendText(op.param1,"you are prohibited from inviting-_-")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':op.param2}
                        PB.sendMessage(c)
        if op.type == 15:
             if op.param2 in admin:
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
        if op.type == 19:
             if op.param2 in Bots:
                   if op.param3 in admin:
                      random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
        if op.type == 19:
             if not op.param2 in Bots:
                   if op.param3 in admin:
                      random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass

                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["protectionOn"] == True:
                   try:
                       klist=[ki,kk,kc,ks,kt]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)
                       X.preventJoinByTicket = True
                       kl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots and admin:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass

                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = PB.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    PB.updateGroup(X)
                    Ti = PB.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        PB1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kd.updateGroup(X)
                    Ticket = kd.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#========================================================================
                if Fmid in op.param3:
                    if op.param2 in Bots and admin:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kh.updateGroup(X)
                    Ti = kh.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kg.updateGroup(X)
                    Ticket = kg.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kj.updateGroup(X)
                    Ti = kj.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kh.updateGroup(X)
                    Ticket = kh.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        PB.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    G = PB.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    PB.updateGroup(G)
                    Ti = PB.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kj.updateGroup(X)
                    Ticket = kj.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Nmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ko.updateGroup(G)
                    Ti = ko.reissueGroupTicket(op.param1)
                    PB.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    PB1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kn.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kn.updateGroup(X)
                    Ti = kn.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


#============================================================================
#------------------------Auto Join-------------------------------
        if op.type == 13:
            if mid in op.param3:
                G = PB.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            PB.rejectGroupInvitation(op.param1)
                        else:
                            PB.acceptGroupInvitation(op.param1)
			    G.preventJoinByTicket = False
			    PB.updateGroup(G)
			    Ticket = PB.reissueGroupTicket(op.param1)
			    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
			    PB1.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
			    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
			    G.preventJoinByTicket = True
			    PB.updateGroup(G)
                    else:
                        PB.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        PB.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    PB.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                PB.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                PB.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            PB.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = PB.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            PB.updateGroup(X)
                        except:
                            PB.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    PB.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                PB.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1001)
                kk.like(url[25:58], url[66:], likeType=1001)
                kc.like(url[25:58], url[66:], likeType=1001)
                PB1.like(url[25:58], url[66:], likeType=1001)
                ks.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        PB.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        PB.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        PB.sendText(msg.to,"Deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        PB.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        PB.sendText(msg.to,"already in the blacklist")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        PB.sendText(msg.to,"successfully load users into the blacklist")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        PB.sendText(msg.to,"successfully removed from the blacklist")

                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        PB.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = PB.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = PB.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        PB.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
                    else:
                        contact = PB.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = PB.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        PB.sendText(msg.to,"⎈ Profile Name :\n" + contact.displayName + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Mesage:\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: メTamii々•┅─────")
            elif msg.contentType == 16:
                if wait["contact"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    PB.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Prank help"]:
              if msg.from_ in admin:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    PB.sendText(msg.to, helpMessage + datetime.today().strftime('%H:%M:%S'))
                else:
                    PB.sendText(msg.to,helpt)
            elif msg.text in ["Key"]:
              if msg.from_ in mid:
                if wait["lang"] == "JP":
                    PB.sendText(msg.to, helpMessage + datetime.today().strftime('%H:%M:%S'))
                else:
                    PB.sendText(msg.to,helpt)
            elif ("Group name:" in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = PB.getGroup(msg.to)
                    X.name = msg.text.replace("Group name:","")
                    PB.updateGroup(X)
                else:
                    PB.sendText(msg.to,"It can't be used besides the group.")


        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = PB.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 PB.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     PB.findAndAddContactsByMid(target)
                                     PB.inviteIntoGroup(msg.to,[target])
                                     PB.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         PB.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            elif "Invite:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite:"," ")
                PB.findAndAddContactsByMid(midd)
                PB.inviteIntoGroup(msg.to,[midd])

            elif msg.text.lower() == 'contact bot':
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                PB.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                PB1.sendMessage(msg)

#=======================================================


            elif msg.text in ["Contact"]:
	      if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                PB.sendMessage(msg)
            elif msg.text.lower() == 'gift1':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                PB.sendMessage(msg)
            elif msg.text.lower() == 'gift2':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text.lower() == 'gift3':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text.lower() == 'gift4':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text.lower() == 'gift5':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}
                msg.text = None
                kd.sendMessage(msg)
            elif msg.text.lower() == 'gift6':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}
                msg.text = None
                ke.sendMessage(msg)
            elif msg.text.lower() == 'spam gift':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                PB.sendMessage(msg)
                ks.sendMessage(msg)
                PB1.sendMessage(msg)
                PB1.sendMessage(msg)

#==================================================
            elif "All rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("All rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = PB.getProfile()
                    profile.displayName = string
                    PB.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = PB1.getProfile()
                    profile.displayName = string
                    PB1.updateProfile(profile)
                    PB.sendText(msg.to,"change name: "+string+"\nsucces")
            elif msg.text.lower() == 'allbio:':
              if msg.from_ in owner:
                string = msg.text.lower().replace("allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = PB.getProfile()
                    profile.statusMessage = string
                    PB.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = PB1.getProfile()
                    profile.statusMessage = string
                    PB1.updateProfile(profile)
                    PB.sendText(msg.to,"successfully turn it into: " + string + "")
            elif "Bot1 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot1 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = PB.getProfile()
                    profile.displayName = string
                    PB.updateProfile(profile)
                    PB.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot2 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot2 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot3 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot3 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot4 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot4 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot5 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot5 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot6 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot6 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = PB1.getProfile()
                    profile.displayName = string
                    PB1.updateProfile(profile)
                    PB1.sendText(msg.to,"change name: "+string+"\nsucces")
#==================================================
            elif 'lyric ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        PB.sendText(msg.to, hasil)
                except Exception as wak:
                        PB.sendText(msg.to, str(wak))
            elif 'wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      PB.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              PB.sendText(msg.to, pesan)
                          except Exception as e:
                              PB.sendText(msg.to, str(e))
            elif msg.text.lower() == 'bot restart':
              if msg.from_ in admin:
                    print "[Command]Like executed"
                    try:
                        PB.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        PB.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif 'instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    PB.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    PB.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	PB.sendText(msg.to, str(njer))
            elif 'music ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        PB.sendText(msg.to, hasil)
                        PB.sendText(msg.to, "SAMBIL NUNGGU YUK DI SUBCRABE CHANNEL NYA  :-)\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                        PB.sendAudioWithURL(msg.to, song[3])
		except Exception as njer:
		        PB.sendText(msg.to, str(njer))
            elif 'clean invites' in msg.text.lower():
               if msg.from_ in admin:
                if msg.toType == 2:
                    X = PB.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            PB.sendText(msg.to,"No one is inviting。")
                        else:
                            PB.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Can not be used outside the group")
                    else:
                        PB.sendText(msg.to,"Not for use less than group")
#================================================================================
            elif 'clear invites' in msg.text.lower():
	      if msg.from_ in admin:
                if msg.toType == 2:
                    group = PB.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                        PB.sendText(msg.to,"I pretended to cancel and canceled.")
            elif 'link open' in msg.text.lower():
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = PB.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#===========================================================================

            elif 'link close' in msg.text.lower():
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = PB.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#============================================================

            elif msg.text.lower() == 'ginfo':
              if msg.from_ in admin:
                ginfo = PB.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                PB.sendText(msg.to,"[display name]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nmembers:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                PB.sendMessage(msg)
#===============================================================
            elif 'group list' in msg.text.lower():
              if msg.from_ in admin:
                gs = PB.getGroupIdsJoined()
                L = "『 Groups List 』\n"
                for i in gs:
                    L += "[≫] %s \n" % (PB.getGroup(i).name + " | [ " + str(len (PB.getGroup(i).members)) + " ]")
                PB.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif "Invite me" in msg.text:
              if msg.from_ in owner:
                         gid = PB.getGroupIdsJoined()
		         for i in gid:
			        PB.findAndAddContactsByMid(msg.from_)
                                PB.inviteIntoGroup(i,[msg.from_])
			        PB.sendText(msg.to, "successfully invited you to all groups")

            elif "Steal group pict" in msg.text:
              if msg.from_ in admin:
					group = PB.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        PB.sendImageWithURL(msg.to,path)
            elif "Turn off bots" in msg.text:
               if msg.from_ in owner:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
#==================================================================
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = PB.getContact(key1)
                cu = PB.channel.getCover(key1)
                try:
                    PB.sendText(msg.to,contact.statusMessage)
                except:
                    PB.sendText(msg.to,contact.statusMessage)
            elif 'Creator' in msg.text.lower():
              if msg.from_ in admin:
				msg.contentType = 13
				msg.contentMetadata = {'mid': "ufce863f62f40706c01fa4a3c3c4cb096"}
				PB.sendMessage(msg)
				PB.sendText(msg.to,"My Creator ")
            elif "Admin on @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = PB.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        PB.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                PB.sendText(msg.to,"succes add to adminlist")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    PB.sendText(msg.to,"Command denied.")
                    PB.sendText(msg.to,"owner permission required.")
            elif msg.text.lower() == 'admin list':
              if msg.from_ in admin:
                if admin == []:
                       PB.sendText(msg.to,"The adminlist is empty")
                else:
                        PB.sendText(msg.to,"loading...")
                        mc = ""
                        gh = ""
                        for mi_d in owner:
                            mc += "->" +PB.getContact(mi_d).displayName + "\n"
		        for mi_d in admin:
			    gh += "->" +PB.getContact(mi_d).displayName + "\n"
                        PB.sendText(msg.to,"=======OWNER=======\n\n" + mc + "\n=======ADMIN=======\n\n" + gh +"\n=====================\n")
                        print "[Command]Stafflist executed"
            elif "Expel on @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Expel on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = PB.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                PB.sendText(msg.to,"Succes remove admin from adminlist")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    PB.sendText(msg.to,"Command denied.")
                    PB.sendText(msg.to,"owner permission required.")
#==========================================================
            elif 'bot mid' in msg.text.lower():
               if msg.from_ in admin:
			PB.sendText(msg.to,mid)
			PB1.sendText(msg.to,Emid)
 #=======================================================
            elif "Translate-eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-eng ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    PB.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except Exception as error:
                    PB.sendText(msg.to,(error))
            elif "Translate-japan " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-japan ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'ja')
                    PB.sendText(msg.to,trs)
                    print '[Command] Translate japan'
                except Exception as error:
                    PB.sendText(msg.to,(error))
            elif "Translate-thai " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-thai ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'th')
                    PB.sendText(msg.to,trs)
                    print '[Command] Translate thai'
                except Exception as error:
                    PB.sendText(msg.to,(error))
            elif "Translate-idn " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    PB.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except Exception as error:
                    PB.sendText(msg.to,(error))

            elif "Say " in msg.text:
              if msg.from_ in  admin:
				bctxt = msg.text.replace("Say ","")
				PB.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ks.sendText(msg.to,(bctxt))
				PB1.sendText(msg.to,(bctxt))

#======================================
            elif "TL:" in msg.text:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL:","")
                PB.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+PB.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])

#=================================================================
            elif msg.text in ["Protect:hight","protect:hight"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Auto blockqr:off","auto blockqr:off"]:
              if msg.from_ in admin:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Welcome message:on"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"welcome message on")
            elif msg.text in ["Auto blockqr:on","auto blockqr:on"]:
              if msg.from_ in admin:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"Already on")
            elif msg.text in ["Welcome message:off"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Protect:low","Protect:low"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['pname']:
                    PB.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    PB.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = PB.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['pname']:
                    PB.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    PB.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")

            elif "Blockinvite:on" == msg.text:
              if msg.from_ in admin:
				gid = msg.to
				autocancel[gid] = "poni"
				PB.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
            elif "Blockinvite:off" == msg.text:
              if msg.from_ in admin:
				try:
					del autocancel[msg.to]
					PB.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
				except:
					pass
 #================================================================
            elif msg.text in ["Invite user"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 PB.sendText(msg.to,"send contact")
#============================================================
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                PB.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                mmid = PB.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                PB.sendMessage(msg)
            elif "Mc:" in msg.text:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                PB.sendMessage(msg)
#=======================================================
            elif msg.text in ["Auto notice:on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"already activated")
                    else:
                        PB.sendText(msg.to,"enable notifications")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"already activated")
                    else:
                        PB.sendText(msg.to,"enable notifications")

#=========================================================================
            elif msg.text in ["Auto notice:off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"already unactivated")
                    else:
                        PB.sendText(msg.to,"disable notifications")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"already unactivated")
                    else:
                        PB.sendText(msg.to,"disable notifications")

            elif msg.text in ["Auto join:on"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"")
                    else:
                        PB.sendText(msg.to,"already activated")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"enable auto koin")
                    else:
                        PB.sendText(msg.to,"")
            elif msg.text in ["Auto join:off"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"already unactivated")
                    else:
                        PB.sendText(msg.to,"desable auto join")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"already unactivated")
                    else:
                        PB.sendText(msg.to,"desable auto join")

            elif "Gcancel:" in msg.text:
              if msg.from_ in admin:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            PB.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            PB.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            PB.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            PB.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Value is wrong")
                    else:
                        PB.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["Auto leave:on"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"already on")
                    else:
                        PB.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"done")
                    else:
                        PB.sendText(msg.to,"要了开。")
            elif msg.text in ["Auto leave:off"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"already off")
                    else:
                        PB.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"done")
                    else:
                        PB.sendText(msg.to,"already")
#===============================================================

            elif msg.text in ["Auto like:on"]:
              if msg.from_ in admin:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Already。")
            elif msg.text in ["Auto like:off"]:
              if msg.from_ in admin:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Already。")
#==========================================================

            elif msg.text in ["Settings"]:
              if msg.from_ in admin:
            	print "Setting pick up..."
                md="list of bot settings\n\n"
                if wait["likeOn"] == True: md+="Auto like : on\n"
                else:md+="Auto like : off\n"
                if mimic["copy"] == True: md+="Mimic : on\n"
                else:md+="Mimic : off\n"
                if wait["winvite"] == True: md+="Invite : on\n"
                else:md+="Invite : off\n"
                if wait["pname"] == True: md+="Namelock : on\n"
                else:md+="Namelock : off\n"
                if wait["contact"] == True: md+="Notice : on\n"
                else: md+="Notice : off\n"
                if wait["autoJoin"] == True: md+="Auto join : on\n"
                else: md +="Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="Auto leave : on\n"
                else: md+="Auto leave : off\n"
                if wait["clock"] == True: md+="Clock Name : on\n"
                else:md+="Clock Name : off\n"
                if wait["autoAdd"] == True: md+="Auto add : on\n"
                else:md+="Auto add : off\n"
                if wait["commentOn"] == True: md+="Comment : on\n"
                else:md+="Comment : off\n"
                if wait["Backup"] == True: md+="Backup : on\n"
                else:md+="Backup : off\n"
                if wait["qr"] == True: md+="Protect QR : on\n"
                else:md+="Protect QR : off\n"
                if wait["welcomemsg"] == True: md+="welcome message : on\n"
                else:md+="welcome message : off\n"
                if wait["protectionOn"] == True: md+="Protection : hight\n\n"+ datetime.today().strftime('%H:%M:%S')
                else:md+="Protection : low\n\n"+ datetime.today().strftime('%H:%M:%S')
                PB.sendText(msg.to,md)
#========================================
#------------------------------------------------
            elif "Time" in msg.text:
              if msg.from_ in admin:
                  PB.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["PING","Ping","ping"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔Har Har")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔Har Har")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔Har Har")
		ks.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔Har Har")
		PB1.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔Har Har")
		PB.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔Har Har")
            elif "Info @" in msg.text:
              if msg.from_ in admin:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = PB.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        gjh= PB.getContact(g.mid)
                        try:
                            cover = PB.channel.getCover(g.mid)
                        except:
                            cover = ""
                        PB.sendText(msg.to,"[Display Name]:\n" + gjh.displayName + "\n[Mid]:\n" + gjh.mid + "\n[BIO]:\n" + gjh.statusMessage + "\n[pict profile]:\nhttp://dl.profile.line-cdn.net/" + gjh.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
#-----------------------------------------------
            elif msg.text in ["Backup:on"]:
              if msg.from_ in admin:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off"]:
              if msg.from_ in admin:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        PB.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Rejectall"]:
              if msg.from_ in admin:
                gid = PB.getGroupIdsInvited()
                for i in gid:
                    PB.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    PB.sendText(msg.to,"All Invites has been Rejected")
                else:
                    PB.sendText(msg.to,"拒绝了全部的邀请。")

            elif msg.text in ["Auto add:on"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"success activated")
                    else:
                        PB.sendText(msg.to,"success activated")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"success activated")
                    else:
                        PB.sendText(msg.to,"success activated")
            elif msg.text in ["Auto add:off"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"success unactivated")
                    else:
                        PB.sendText(msg.to,"success unactivated")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"success unactivated")
                    else:
                        PB.sendText(msg.to,"success unactivated")
#========================================
#========================================
            elif "Update welcome:" in msg.text:
              if msg.from_ in admin:
                wait["welmsg"] = msg.text.replace("Update welcome:","")
                PB.sendText(msg.to,"update welcome message succes"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check welcome message"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    PB.sendText(msg.to,"yor bot message\n\n" + wait["welmsg"])
                else:
                    PB.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])
            elif "Message:" in msg.text:
              if msg.from_ in admin:
                wait["message"] = msg.text.replace("Message:","")
                PB.sendText(msg.to,"bot message\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Add message:" in msg.text:
              if msg.from_ in admin:
                wait["message"] = msg.text.replace("Add message:","")
                if wait["lang"] == "JP":
                    PB.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    PB.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check message"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    PB.sendText(msg.to,"yor bot message\n\n" + wait["message"])
                else:
                    PB.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
            elif "Comment:" in msg.text:
              if msg.from_ in admin:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    PB.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    PB.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
              if msg.from_ in admin:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    PB.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    PB.sendText(msg.to,"changed\n\n" + c)

            elif msg.text in ["Comment:on"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Done")
                    else:
                        PB.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Done")
                    else:
                        PB.sendText(msg.to,"Already on")
            elif msg.text in ["Comment:off"]:
              if msg.from_ in admin:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Done")
                    else:
                        PB.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        PB.sendText(msg.to,"Done")
                    else:
                        PB.sendText(msg.to,"Already off")
            elif msg.text in ["Check comment"]:
              if msg.from_ in admin:
                PB.sendText(msg.to,"message comment\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    x = PB.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        uye.updateGroup(x)
                    gurl = uye.reissueGroupTicket(msg.to)
                    uye.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#===========================================
            elif msg.text.lower() == 'responsename':
              if msg.from_ in admin:
                profile = PB.getProfile()
                text = profile.displayName + ""
                PB.sendText(msg.to, text)
                profile = ki.getProfile()
                text = profile.displayName + ""
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + ""
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + ""
                kc.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName + ""
                ks.sendText(msg.to, text)
                profile = PB1.getProfile()
                text = profile.displayName + ""
                PB1.sendText(msg.to, text)

#========================================
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                PB.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                PB.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    PB.sendText(msg.to,"confirmed")
                else:
                    PB.sendText(msg.to,"Blacklist s")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +PB.getContact(mi_d).displayName + "\n"
                    PB.sendText(msg.to,mc)

            elif msg.text in ["Clock:on","Clock on","Jam on","Jam:on"]:
                if wait["clock"] == True:
                    PB.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"[%H:%M]")
                    profile = PB.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    PB.updateProfile(profile)
                    PB.sendText(msg.to,"done")

            elif msg.text in ["Clock:off","Clock off","Jam off","Jam:off"]:
                if wait["clock"] == False:
                    PB.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    PB.sendText(msg.to,"done")

            elif "Cc: " in msg.text:
                n = msg.text.replace("Cc: ","")
                if len(n.decode("utf-8")) > 13:
                    PB.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    PB.sendText(msg.to,"Changed to:\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"[%H:%M]")
                    profile = PB.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    PB.updateProfile(profile)
                    PB.sendText(msg.to,"Refresh to update")
                else:
                    PB.sendText(msg.to,"Please turn on the name clock")

#========================================
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = PB.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    PB.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = PB.getContact(target)
                            cu = PB.channel.getCover(target)
                            path = str(cu)
                            PB.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midpict:","")
                contact = PB.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    PB.sendImageWithURL(msg.to,image)
                except Exception as error:
                    PB.sendText(msg.to,(error))
                    pass
            elif "Steal pict " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = PB.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        PB.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = PB.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    PB.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    PB.sendText(msg.to,(error))
                                    pass
                            except:
                                PB.sendText(msg.to,"Error!")
                                break
                else:
                    PB.sendText(msg.to,"Tidak bisa dilakukan di luar grup")

#===============================================
            elif msg.text in ["debug speed","Debug speed"]:
              if msg.from_ in admin:
                PB.sendText(msg.to, "Measuring...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                PB.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu executed"


            elif msg.text in ["Speed","speed"]:
	      if msg.from_ in admin:
                start = time.time()
                PB.sendText(msg.to, "loading...................")
                elapsed_time = time.time() - start
                PB.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki.sendText(msg.to, "%sseconds" % (elapsed_time))
		kk.sendText(msg.to, "%sseconds" % (elapsed_time))
		kc.sendText(msg.to, "%sseconds" % (elapsed_time))
		ks.sendText(msg.to, "%sseconds" % (elapsed_time))
		PB1.sendText(msg.to, "%sseconds" % (elapsed_time))
#========================================
            elif msg.text in ["Bot1 backup run"]:
                if msg.from_ in admin:
                    wek = PB.getContact(mid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myps.txt',"w")
                    u.write(a)
                    u.close()
                    PB.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot2 backup run"]:
                if msg.from_ in admin:
                    wek = ki.getContact(Amid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myesm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfs.txt',"w")
                    u.write(a)
                    u.close()
                    ki.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot3 backup run"]:
                if msg.from_ in admin:
                    wek = kk.getContact(Bmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('msgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysfdgm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('gymyps.txt',"w")
                    u.write(a)
                    u.close()
                    kk.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot4 backup run"]:
                if msg.from_ in admin:
                    wek = kc.getContact(Cmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('jhmydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myhfsm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfhs.txt',"w")
                    u.write(a)
                    u.close()
                    kc.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot5 backup run"]:
                if msg.from_ in admin:
                    wek = ks.getContact(Dmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('madydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysgjm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myrdps.txt',"w")
                    u.write(a)
                    u.close()
                    ks.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot6 backup run"]:
                if msg.from_ in admin:
                    wek = PB1.getContact(Emid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydnsgv.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('jhmysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myiyps.txt',"w")
                    u.write(a)
                    u.close()
                    PB1.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
#----------------------------------------------
            elif "Bot1 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = PB.getContact(target)
                        X = contact.displayName
                        profile = PB.getProfile()
                        profile.displayName = X
                        PB.updateProfile(profile)
                        PB.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = PB.getProfile()
                        lol.statusMessage = Y
                        PB.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        PB.updateProfilePicture(P)
                    except Exception as e:
                        PB.sendText(msg.to, "Failed!")
                        print e
            elif "Bot2 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = ki.getContact(target)
                        X = contact.displayName
                        profile = ki.getProfile()
                        profile.displayName = X
                        ki.updateProfile(profile)
                        ki.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = ki.getProfile()
                        lol.statusMessage = Y
                        ki.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        ki.updateProfilePicture(P)
                    except Exception as e:
                        ki.sendText(msg.to, "Failed!")
                        print e
            elif "Bot3 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kk.getContact(target)
                        X = contact.displayName
                        profile = kk.getProfile()
                        profile.displayName = X
                        kk.updateProfile(profile)
                        kk.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kk.getProfile()
                        lol.statusMessage = Y
                        kk.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kk.updateProfilePicture(P)
                    except Exception as e:
                        kk.sendText(msg.to, "Failed!")
                        print e
            elif "Bot4 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kc.getContact(target)
                        X = contact.displayName
                        profile = kc.getProfile()
                        profile.displayName = X
                        kc.updateProfile(profile)
                        kc.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kc.getProfile()
                        lol.statusMessage = Y
                        kc.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kc.updateProfilePicture(P)
                    except Exception as e:
                        kc.sendText(msg.to, "Failed!")
                        print e
            elif "Bot5 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = ks.getContact(target)
                        X = contact.displayName
                        profile = ks.getProfile()
                        profile.displayName = X
                        ks.updateProfile(profile)
                        ks.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = ks.getProfile()
                        lol.statusMessage = Y
                        ks.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        ks.updateProfilePicture(P)
                    except Exception as e:
                        ks.sendText(msg.to, "Failed!")
                        print e
            elif "Bot6 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = PB1.getContact(target)
                        X = contact.displayName
                        profile = PB1.getProfile()
                        profile.displayName = X
                        PB1.updateProfile(profile)
                        PB1.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = PB1.getProfile()
                        lol.statusMessage = Y
                        PB1.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        PB1.updateProfilePicture(P)
                    except Exception as e:
                        PB1.sendText(msg.to, "Failed!")
                        print e

#=================================================
            elif "Bot1 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('mydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = PB.getProfile()
                            profile.displayName = x
                            PB.updateProfile(profile)
                            i = open('mysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = PB.getProfile()
                            cak.statusMessage = y
                            PB.updateProfile(cak)
                            j = open('myps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            PB.updateProfilePicture(p)
                            PB.sendText(msg.to, "Succes")
                        except Exception as e:
                            PB.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot2 backup" in msg.text:
                 if msg.from_ in admin:
                        try:
                            h = open('mgydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = ki.getProfile()
                            profile.displayName = x
                            ki.updateProfile(profile)
                            i = open('myesm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = ki.getProfile()
                            cak.statusMessage = y
                            ki.updateProfile(cak)
                            j = open('mypfs.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            ki.updateProfilePicture(p)
                            ki.sendText(msg.to, "Succes")
                        except Exception as e:
                            ki.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot3 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('msgydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kk.getProfile()
                            profile.displayName = x
                            kk.updateProfile(profile)
                            i = open('mysfdgm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kk.getProfile()
                            cak.statusMessage = y
                            kk.updateProfile(cak)
                            j = open('gymyps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kk.updateProfilePicture(p)
                            kk.sendText(msg.to, "Succes")
                        except Exception as e:
                            kk.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot4 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('jhmydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kc.getProfile()
                            profile.displayName = x
                            kc.updateProfile(profile)
                            i = open('myhfsm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kc.getProfile()
                            cak.statusMessage = y
                            kc.updateProfile(cak)
                            j = open('mypfhs.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kc.updateProfilePicture(p)
                            kc.sendText(msg.to, "Succes")
                        except Exception as e:
                            kc.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot5 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('madydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = ks.getProfile()
                            profile.displayName = x
                            ks.updateProfile(profile)
                            i = open('mysgjm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = ks.getProfile()
                            cak.statusMessage = y
                            ks.updateProfile(cak)
                            j = open('myrdps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            ks.updateProfilePicture(p)
                            ks.sendText(msg.to, "Succes")
                        except Exception as e:
                            ks.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot6 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('mydnsgv.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = PB1.getProfile()
                            profile.displayName = x
                            PB1.updateProfile(profile)
                            i = open('jhmysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = PB1.getProfile()
                            cak.statusMessage = y
                            PB1.updateProfile(cak)
                            j = open('myiyps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            PB1.updateProfilePicture(p)
                            PB1.sendText(msg.to, "Succes")
                        except Exception as e:
                            PB1.sendText(msg.to,"Gagagl!")
                            print e
#=================================================
            elif msg.text == "Lurking":
              if msg.from_ in admin:
                    PB.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Lurking result":
              if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        PB.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        PB.sendText(msg.to, "anda slah ketik-_-")

#========================================
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
            elif "Fuckyou" in msg.text:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok cleanse"
                    _name = msg.text.replace("Fuckyou","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    PB.sendText(msg.to,"Just some casual cleansing ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"you are not admin")
                    else:
                        for target in targets:
                          if not target in Bots:
                            if not target in admin:
                               try:
                                klist=[ki,kk,kc,ks,kt]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                               except:
                                PB.sendText(msg.to,"Group cleanse")
#================================================
#========================================
            elif msg.text.lower() == 'welcome':
              if msg.from_ in admin:
                ginfo = PB.getGroup(msg.to)
                PB.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                PB.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#=======================================
#-------------------Fungsi spam start--------------------------
            elif "Spam change:" in msg.text:
              if msg.from_ in admin:
                wait["spam"] = msg.text.replace("Spam change:","")
                PB.sendText(msg.to,"spam changed")

            elif "Spam add:" in msg.text:
              if msg.from_ in admin:
                wait["spam"] = msg.text.replace("Spam add:","")
                if wait["lang"] == "JP":
                    PB.sendText(msg.to,"spam changed")
                else:
                    PB.sendText(msg.to,"Done")

            elif "Spam:" in msg.text:
              if msg.from_ in admin:
                strnum = msg.text.replace("Spam:","")
                num = int(strnum)
                for var in range(0,num):
                    PB.sendText(msg.to, wait["spam"])

#-------------------Fungsi spam finish----------------------------
#-----------------------------------------------
#-----------------------------------------------
            elif 'apakah' in msg.text.lower():
              if msg.from_ in admin:
                tanya = msg.text.lower().replace("apakah","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                jawaban = random.choice(jawab)
                PB.sendText(msg.to,jawaban)

#================================================
#===============================================
#=================================================
            elif "Spamg " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spamg "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   PB.sendText(msg.to, teks)
                        else:
                               PB.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               PB.sendText(msg.to, tulisan)
                         else:
                               PB.sendText(msg.to, "Out of range! ")
#-----------------------------------------------
            elif "Steal mid @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Steal mid @","")
                _nametarget = _name.rstrip(' ')
                gs = PB.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        PB.sendText(msg.to, g.mid)
                    else:
                        pass
#-------------------------------------------------
            elif "Pm cast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = PB.getAllContactIds()
					for manusia in t:
						PB.sendText(manusia,(bctxt))
            elif "Broadcast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Broadcast ", "")
					n = PB.getGroupIdsJoined()
					for manusia in n:
						PB.sendText(manusia,(bctxt +"\n\n\nbroadcasted by:" + PB.getContact(msg.from_).displayName))

#========================================
            elif msg.text in ["Prank in"]:
              if msg.from_ in admin:
					G = PB.getGroup(msg.to)
					info = PB.getGroup(msg.to)
					G.preventJoinByTicket = False
					PB.updateGroup(G)
					invsend = 0
					Ticket = PB.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					kk.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					kc.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					ks.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
                                        PB1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
					G = PB.getGroup(msg.to)
					G.preventJoinByTicket = True
					PB.updateGroup(G)
					print "All_Kickers_Ok!"
					G.preventJoinByTicket(G)
					PB.updateGroup(G)
#=====================================================================================

            elif msg.text in ["Bye allgroups"]:
              if msg.from_ in admin:
				gid = PB.getGroupIdsJoined()
				for i in gid:
					PB.leaveGroup(i)
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
					ks.leaveGroup(i)
					PB1.leaveGroup(i)
				if wait["lang"] == "JP":
					ki.sendText(msg.to,"bye-bye")
				else:
					ki.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Prank @bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                   X = PB.getGroup(msg.to)
                try:
                     ki.leaveGroup(msg.to)
                     kk.leaveGroup(msg.to)
                     kc.leaveGroup(msg.to)
                     ks.leaveGroup(msg.to)
                     PB1.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Center @bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                   X = PB.getGroup(msg.to)
                try:
                    # PB.sendMessage(msg.to,"bye-bye")
                     PB.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Nk "]:
              if msg.from_ in admin:
                       mk0 = msg.text.replace("Nk ","")
                       mk1 = mk0.lstrip()
                       mk2 = mk1.replace("@","")
                       mk3 = mk2.rstrip()
                       _name = mk3
                       gs = ki.getGroup(msg.to)
                       targets = []
                       for h in gs.members:
                           if _name in h.displayName:
                              targets.append(h.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                               try:
                                 if msg.from_ not in target:
                                   ki.kickoutFromGroup(msg.to,[target])
                               except:
			           random.choice(KAC).kickoutFromGroup(msg.to,[target])

#==========================================
            elif "Youtube " in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           PB.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           PB.sendText(msg.to, isi[0])
                   except Exception as e:
                       PB.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
	      if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Vidio ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    PB.sendVideoWithURL(msg.to,ght)
                except:
                    PB.sendText(msg.to,"Could not find it")
#==========================================
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:

            	    ki.sendText(msg.to,text)
                    kc.sendText(msg.to,text)
                    kk.sendText(msg.to,text)
                    ks.sendText(msg.to,text)
                    PB1.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			kk.sendMessage(msg)
            			ki.sendMessage(msg)
			        kc.sendMessage(msg)
            			ks.sendMessage(msg)
			        PB1.sendMessage(msg)

            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			kk.sendMessage(msg)
            			ki.sendMessage(msg)
                                PB1.sendMessage(msg)
                                kc.sendMessage(msg)
                                ks.sendMessage(msg)


            elif msg.text in ["Target list"]:
              if msg.from_ in admin:
                        if mimic["target"] == {}:
                            PB.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "✔️ "+PB.getContact(mi_d).displayName + "\n"
                            PB.sendText(msg.to,mc)


            elif "Mimic:" in msg.text:
	          if msg.from_ in admin:
            		  cmd = msg.text.replace("Mimic:","")
            		  if cmd == "on":
            			  if mimic["status"] == False:
            				  mimic["status"] = True
            				  PB.sendText(msg.to,"turning on mimic")

            			  else:
            				  PB.sendText(msg.to,"mimic have been enable")

            		  elif cmd == "off":
            			  if mimic["status"] == True:
            				  mimic["status"] = False
            				  PB.sendText(msg.to,"turning off mimic")

            			  else:
            				  PB.sendText(msg.to,"Mimic have been desable")

            		  elif "target " in cmd:
                            if msg.from_ in admin:
                                      target0 = msg.text.replace("Mimic target ","")
            			      target1 = target0.lstrip()
            			      target2 = target1.replace("@","")
            			      target3 = target2.rstrip()
            			      _name = target3
            			      gInfo = PB.getGroup(msg.to)
            			      targets = []
            			      for a in gInfo.members:
                               	              if _name == a.displayName:
            				              targets.append(a.mid)
            			      if targets == []:
            				     PB.sendText(msg.to,"No targets")

            			      else:
                			      for target in targets:
            					      try:
            						      mimic["target"][target] = True
            						      PB.sendText(msg.to,"Success added target")

            						      #PB.sendMessageWithMention(msg.to,target)
            						      break
            					      except:
            						      PB.sendText(msg.to,"Failed")

            						      break
            		  elif "untarget " in cmd:
                            if msg.from_ in admin:
            			      target0 = msg.text.replace("Mimic untarget ","")
            			      target1 = target0.lstrip()
            			      target2 = target1.replace("@","")
            			      target3 = target2.rstrip()
            			      _name = target3
            			      gInfo = PB.getGroup(msg.to)
            			      gInfo = ki.getGroup(msg.to)
            			      targets = []
            			      for a in gInfo.members:
            				      if _name == a.displayName:
            					      targets.append(a.mid)
            			      if targets == []:
            				      PB.sendText(msg.to,"No targets")

            			      else:
            				      for target in targets:
            					      try:
            						      del mimic["target"][target]
            						      PB.sendText(msg.to,"Success deleted target")

            						      #PB.sendMessageWithMention(msg.to,target)
            						      break
            					      except:
            						      PB.sendText(msg.to,"Failed!")

#==========================================
            elif msg.text in ["Purge"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = PB.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"group purge")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,ks,kt]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass

            elif ("Vkick" in msg.text):
				if msg.from_ in admin:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							PB.kickoutFromGroup(msg.to,[target])
						except:
							PB.sendText(msg.to,"Error")



#-----------------------------------------------------------



            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = PB.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        PB.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                PB.sendText(msg.to,"Success Masuk daftar orang bejat Boss")
                            except:
                                PB.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = PB.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        PB.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                PB.sendText(msg.to,"Sudah di keluarkan dari daftar bejat Boss")
                            except:
                                PB.sendText(msg.to,"There was no blacklist user")
            elif msg.text in ["Clear banlist"]:
              if msg.from_ in admin:
				wait["blacklist"] = {}
				PB.sendText(msg.to,"succes clear all banlist")

            elif msg.text in ["Banned"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                PB.sendText(msg.to,"send contact to ban")

            elif msg.text in ["Unbanned"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                PB.sendText(msg.to,"send contact to ban")

            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    PB.sendText(msg.to,"nothing")
                else:
                    PB.sendText(msg.to,"blacklist user list")
                    mc = "[⎈]Blacklist User[⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + PB.getContact(mi_d).displayName + " \n"
                    PB.sendText(msg.to, mc + "")


#=============================================

# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Ban repeat " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      PB.sendText(msg.to,"Succes Banned ")
                   except:
                      pass
#-------------------------------------------------------------
            elif msg.text in ["Pranktag"]:
	            #if msg.from_ in admin:
                group = PB.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    PB.sendMessage(msg)
#-------------------FUNGSI TAGALL---------------#
        if op.param3 == "1":
            if op.param1 in protectname:
                group = PB.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					PB.updateGroup(group)
					PB.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = ""
			if op.param2 in Bots and admin:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = PB.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				PB1.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#===========================================
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = PB.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n╠" + Name
						wait2['ROM'][op.param1][op.param2] = "╠" + Name
				else:
					PB.sendText
            except:
                pass


#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in PB.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   PB.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ks.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   PB1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          PB.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kc.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ks.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          PB1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = PB.getProfile()
                profile.displayName = wait["cName"] + nowT
                PB.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = PB.fetchOps(PB.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(PB.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            PB.Poll.rev = max(PB.Poll.rev, Op.revision)
            bot(Op)

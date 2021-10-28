import socket
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import pymysql
from email_validator import validate_email
from pathlib import Path

path = str(Path.cwd())

connection = pymysql.connect() # Database inforamtions ( not in github )
cursor = connection.cursor()

words = ['scarf', 'possible', 'lettuce', 'voice', 'rainstorm', 'loving', 'extra-small', 'flagrant', 'ambiguous', 'trains', 'yard', 'godly', 'lighten', 'nutritious', 'rod', 'toys', 'greedy', 'belief', 'behavior', 'alike', 'lively', 'kneel', 'oafish', 'squirrel', 'energetic', 'dinner', 'crime', 'chalk', 'dam', 'bomb', 'mourn', 'detect', 'onerous', 'rabid', 'chase', 'tap', 'unsuitable', 'texture', 'change', 'mute', 'bit', 'payment', 'sink', 'cows', 'hushed', 'fat', 'flock', 'cent', 'roasted', 'obtain', 'prepare', 'letter', 'bushes', 'fax', 'heat', 'subdued', 'cold', 'nod', 'snobbish', 'pin', 'wrathful', 'flood', 'comb', 'airplane', 'visitor', 'frightening', 'maid', 'knife', 'hideous', 'previous', 'glue', 'pancake', 'round', 'tempt', 'peel', 'habitual', 'moldy', 'fold', 'icy', 'digestion', 'minister', 'reject', 'race', 'flap', 'yam', 'gullible', 'obsequious', 
'welcome', 'grape', 'grey', 'border', 'bone', 'identify', 'dysfunctional', 'destruction', 'repair', 'system', 'tidy', 'terrible', 'branch', 'imperfect', 'like', 'add', 'pale', 'glistening', 'charge', 'splendid', 'swim', 'unwritten', 'juicy', 'reflect', 'public', 'hobbies', 'tumble', 'abortive', 'cloistered', 'thought', 'whine', 'bashful', 'actor', 'scattered', 'flashy', 'slippery', 'pear', 'accessible', 'rat', 'fuzzy', 'pop', 
'early', 'fireman', 'calendar', 'leather', 'overt', 'shiny', 'lip', 'bath', 'substantial', 'education', 'hose', 'recognise', 'tub', 'women', 'holiday', 'jellyfish', 'nauseating', 'shy', 'jeans', 'fumbling', 'shivering', 'play', 'post', 'awake', 'reproduce', 'work', 'grandfather', 'smash', 'attack', 'mailbox', 'tense', 'cap', 'awful', 'rake', 'sudden', 'verse', 'spray', 'puzzling', 'apparatus', 'wind', 'happy', 'null', 'pray', 
'legal', 'degree', 'truck', 'labored', 'stranger', 'sticks', 'curved', 'tremendous', 'nimble', 'erratic', 'statement', 'brick', 'blink', 'earsplitting', 'protect', 'bounce', 'happen', 'plough', 'decisive', 'page', 'fence', 'mint', 'waste', 'weight', 'complain', 'stale', 'imagine', 'stormy', 'horn', 'cow', 'aboriginal', 'gate', 'tent', 'children', 'chop', 'vegetable', 'boorish', 'important', 'greet', 'evanescent', 'locket', 'crowded', 'knowledgeable', 'truculent', 'loud', 'haunt', 'religion', 'show', 'suck', 'tranquil', 'lethal', 'trot', 'mass', 'delight', 'tricky', 'cracker', 'separate', 'glossy', 'doubt', 'belong', 'zebra', 'relation', 
'window', 'vagabond', 'marry', 'blood', 'obnoxious', 'basket', 'ring', 'flippant', 'kick', 'bore', 'painful', 'threatening', 'sound', 'stupendous', 'ordinary', 'pick', 'challenge', 'brawny', 'birth', 'horse', 'physical', 'coat', 'underwear', 'queen', 'utter', 'peep', 'planes', 'calm', 'agonizing', 'dislike', 'high-pitched', 'art', 'turkey', 'grouchy', 'direction', 'kitty', 'wasteful', 'iron', 'receive', 'baseball', 'fruit', 'wren', 'striped', 'creator', 'well-groomed', 'lace', 'woebegone', 'friends', 'abundant', 'savory', 'wealthy', 'tooth', 'prevent', 'rule', 'wish', 'veil', 'book', 'toad', 'unwieldy', 'comparison', 'jog', 'breezy', 'tow', 'company', 'tired', 'rose', 'melt', 'longing', 'eight', 'ink', 'astonishing', 'telling', 'stimulating', 'bizarre', 'pleasant', 'aquatic', 'clear', 'yawn', 'injure', 'utopian', 'observation', 'concern', 'force', 
'zesty', 'discussion', 'reading', 'moor', 'wealth', 'value', 'drum', 'mundane', 'symptomatic', 'confess', 'cat', 'excellent', 'robin', 'permissible', 'dark', 'approve', 'capricious', 'unnatural', 'star', 'thunder', 
'fanatical', 'unaccountable', 'person', 'nippy', 'freezing', 'common', 'heavy', 'grade', 'preach', 'balance', 'rub', 'scorch', 'needle', 'worried', 'scary', 'daily', 'worry', 'circle', 'wood', 'skip', 'powder', 'substance', 'pointless', 'arrange', 'lyrical', 'replace', 'guide', 'obtainable', 'rambunctious', 'sky', 'last', 'cooing', 'rings', 'cautious', 'snotty', 'playground', 'abject', 'error', 'approval', 'harass', 'activity', 'abrasive', 'vest', 'wise', 'cannon', 'few', 'magnificent', 'wiry', 'water', 'disapprove', 'vivacious', 'potato', 'typical', 'well-to-do', 'channel', 'kill', 'whistle', 'beneficial', 'uppity', 'duck', 'worm', 'treat', 'noxious', 'hover', 'distance', 'furniture', 'explain', 'abashed', 'laughable', 'cynical', 'oil', 'coordinated', 'notebook', 'gray', 'pizzas', 'breakable', 'seed', 'classy', 'stain', 'royal', 'impulse', 'downtown', 'scarce', 'possessive', 'pie', 'paltry', 'blow', 'needless', 'acceptable', 'cause', 'barbarous', 'wholesale', 'lunchroom', 'gold', 'courageous', 'exciting', 'dead', 'spicy', 'town', 'suppose', 'war', 'attend', 
'guitar', 'earthy', 'soothe', 'night', 'combative', 'sister', 'measure', 'vase', 'macho', 'cats', 'cycle', 'fetch', 'telephone', 'yellow', 'roll', 'productive', 'chilly', 'mug', 'dance', 'quixotic', 'helpful', 'momentous', 'ghost', 'maniacal', 'tight', 'draconian', 'tough', 'bury', 'wiggly', 'cherry', 'cool', 'rain', 'end', 'sloppy', 'filthy', 'half', 'innocent', 'odd', 'bang', 'tire', 'messy', 'cheer', 'educated', 'spooky', 'equable', 'weary', 'want', 'quicksand', 'expect', 'jewel', 'hang', 'occur', 'bottle', 'bedroom', 'can', 'sand', 'efficacious', 'size', 'trap', 'ossified', 'deadpan', 'nervous', 'quartz', 'doll', 'careless', 'bridge', 'ugly', 'handy', 'adventurous', 'saw', 'useless', 'please', 'friend', 'bell', 'amused', 'high', 'wait', 'trade', 'craven', 'aromatic', 'imported', 'vengeful', 'huge', 'sneaky', 'spare', 'aggressive', 'notice', 'design', 'flawless', 'gather', 'cry', 'fade', 'relax', 'burst', 'punish', 'first', 'compete', 'many', 'stocking', 'wry', 'capable', 'holistic', 'optimal', 'sense', 'canvas', 'dry', 'school', 'nation', 'vigorous', 'frightened', 'tasteless', 'slap', 'kiss', 'idea', 'thaw', 'pets', 'nostalgic', 'real', 'knotty', 'beginner', 'awesome', 'needy', 'fit', 'comfortable', 'dream', 'silent', 'loutish', 'ladybug', 'servant', 'measly', 'closed', 'confused', 'spot', 'deserted', 'uneven', 'allow', 'immense', 'rabbits', 'defective', 'wacky', 'swanky', 'fallacious', 'aunt', 'mighty', 'amount', 'check', 'pine', 'ancient', 'square', 'annoyed', 'borrow', 'wilderness', 'shocking', 'rare', 'spill', 'quiet', 'great', 'scintillating', 'gratis', 'act', 'uttermost', 'memorize', 'cute', 'correct', 'absent', 'zonked', 'offer', 'waggish', 'jam', 'argument', 'invite', 'ruddy', 'brief', 'addition', 'level', 'obscene', 'itch', 'respect', 'unite', 'side', 'kettle', 'treatment', 'wobble', 'strengthen', 'cruel', 'callous', 'satisfying', 'disagree', 'ambitious', 'lumpy', 'unadvised', 'grotesque', 'lame', 'introduce', 'consider', 'division', 'rude', 'mellow', 'arrest', 'poised', 'protest', 'thoughtless', 'ugliest', 'impolite', 'eggs', 'bucket', 'womanly', 'passenger', 'shoe', 'flight', 'dust', 'marvelous', 'fluttering', 'pink', 'transport', 'men', 'cuddly', 'slim', 'illegal', 'steep', 'remember', 'pushy', 'modern', 'pedal', 'glib', 'twist', 'interesting', 'attach', 'abrupt', 'arrive', 'group', 'bouncy', 'little', 'judge', 'reward', 'five', 'possess', 'groovy', 'dirt', 'connect', 'bumpy', 'plucky', 'rustic', 'grip', 'object', 'old-fashioned', 'unused', 'undress', 'good', 'bite-sized', 'health', 'exuberant', 'even', 'unable', 'pocket', 'knee', 'advise', 'suspect', 'interest', 'stream', 'tremble', 'plug', 'rejoice', 'calculator', 'silky', 'afterthought', 'feeble', 'voracious', 'nutty', 'lie', 'woozy', 'representative', 'taste', 'houses', 'temporary', 'crabby', 'wrong', 'partner', 'bare', 'wandering', 'oven', 'snail', 'extra-large', 'elderly', 'witty', 'toy', 'soft', 'spectacular', 'statuesque', 'gamy', 'crowd', 'continue', 'diligent', 'decision', 'boring', 'scratch', 'loose', 'lucky', 'analyze', 'chicken', 'cushion', 'riddle', 'caption', 'road', 'makeshift', 'soggy', 'calculating', 'decide', 'plants', 'house', 'butter', 'double', 'thin', 'badge', 'soda', 'examine', 'low', 'selection', 'sweater', 'sleet', 'violet', 'fish', 'skillful', 'wail', 'nine', 'rainy', 'busy', 'precious', 'invincible', 'detail', 'sign', 'boiling', 'knot', 'next', 'color', 'vague', 'delay', 'clean', 'harbor', 'oranges', 'crayon', 'tender', 'disagreeable', 'file', 'muddled', 'feigned', 'warm', 'afraid', 'rot', 'mate', 'nebulous', 'daughter', 'icicle', 'rigid', 'trees', 'piquant', 'card', 'impress', 'hallowed', 'machine', 'ruthless', 'imaginary', 'egg', 'apparel', 'advice', 'equal', 'example', 'agreeable', 'run', 'hug', 'switch', 'encourage', 'true', 'tenuous', 'shade', 'faithful', 'electric', 'near', 'humdrum', 'powerful', 'grandiose', 'touch', 'intelligent', 'eatable', 'quickest', 'dispensable', 'well-made', 'absorbing', 'embarrassed', 'copper', 'irritating', 'turn', 'railway', 'agree', 'wine', 'cattle', 'suffer', 'blade', 'carve', 'flower', 'library', 'quince', 'watch', 'berry', 'rebel', 'corn', 'disgusted', 'towering', 'vulgar', 'wave', 'babies', 'knowing', 'uninterested', 'wriggle', 'thoughtful', 'drab', 'improve', 'back', 'pail', 'story', 'lamentable', 'swift', 'teaching', 'sleep', 'hulking', 'calculate', 'stew', 'pan', 'church', 'inject', 'line', 'button', 'boot', 'taboo', 'unfasten', 'curtain', 'bubble', 'view', 'terrific', 'minor', 'charming', 'umbrella', 'cloth', 'terrify', 'simple', 'condemned', 'premium', 'voiceless', 'unkempt', 'spiders', 'dizzy', 'stupid', 'reason', 'cheerful', 'slope', 'record', 'plate', 'orange', 'old', 'panicky', 'unknown', 'anger', 'mark', 'perform', 'festive', 'girl', 'chemical', 'space', 'pleasure', 'absurd', 'silly', 'invention', 'frantic', 'zoom', 'frequent', 'entertain', 'press', 'strip', 'chew', 'stroke', 'cooperative', 'belligerent', 'hand', 'remarkable', 'fry', 'crook', 'heavenly', 'chickens', 'position', 'zealous', 'assorted', 'answer', 'wink', 'admit', 'blind', 'sisters', 'burly', 'plantation', 'bat', 'flowers', 'hospital', 'event', 'mother', 'day', 'jelly', 'label', 'ritzy', 'sturdy', 'plastic', 'chance', 'guard', 'applaud', 'wipe', 'chess', 'short', 'seal', 'camera', 'insurance', 'license', 'rob', 'pies', 'black-and-white', 'songs', 'move', 'dirty', 'desire', 'second-hand', 'decorous', 'dinosaurs', 'observe', 'lunch', 'gainful', 'eminent', 'mountain', 'worthless', 'crazy', 'hole', 'stretch', 'large', 'opposite', 'far-flung', 'conscious', 'mist', 'ship', 'talented', 'omniscient', 'glamorous', 'stingy', 'crash', 'placid', 'tomatoes']

from mainpage import Ui_MainWindow
from login import Ui_LonginWindow
from signup import Ui_SignupWindow
from acountSettings import Ui_AcountSettings

class AcountSettingsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_AcountSettings()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = AcountSettingsWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class SignupWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = SignupWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_LonginWindow()
        self.ui.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def borders(self):
        self.mainwindow = LoginWindow()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.main = Ui_MainWindow()
        self.main.setupUi(self)

        # removing borders
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #===========================My codes===================
        
        # windows
        self.login = LoginWindow()
        self.signup = SignupWindow()
        self.acountsettings = AcountSettingsWindow()

        # get ips from database | check if its new or not
        cursor.execute("SELECT ip FROM acounts;")
        self.ips = []
        for ip in cursor:
            self.ips.append(ip[0])

        self.userip = str(socket.gethostname())
        if self.userip in self.ips:
            self.openMainWindow('username')
        else:
            self.logingin()

    #===============================Designer codes=============
    def borders(self):
        self.mainwindow = RootMain()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    #===============================My funcitons================
    
    # open signin or login page
    def logingin(self):

        def LoginToDB():
            correct_info = True

            # check blanks
            if ((self.login.ui.username_en.text()).strip() == '') or ((self.login.ui.password_en.text()).strip() == ''):
                self.login.ui.alarmlb.setText('Fill all blanks')
            else:
                # check username
                cursor.execute("SELECT username FROM acounts;")
                db_usernames = []
                for username in cursor:
                     db_usernames.append(username[0])
                if self.login.ui.username_en.text() not in db_usernames:
                    self.login.ui.alarmlb.setText('Username does not exists')
                    correct_info = False

                else:
                    # check password
                    cursor.execute("SELECT password FROM acounts WHERE username=\'%s\' ;" % self.login.ui.username_en.text())
                    password = ''
                    for row in cursor:
                        password = row[0]

                    if self.login.ui.password_en.text() != password:
                        self.login.ui.alarmlb.setText('Username or Password is not correct')
                        correct_info = False

            # change user ip in database
            if correct_info == True:
                quary = "UPDATE acounts SET ip=\'%s\' WHERE username=\'%s\' ;" % (str(socket.gethostname()) , self.login.ui.username_en.text())
                cursor.execute(quary)
                connection.commit()

                self.openMainWindow(self.login.ui.username_en.text())

        # sign in page
        def signing():
            self.login.close()
            self.signup.show()

            def putInfoToDB():

                # check infos
                correct_info = True

                # check blanks
                if ((self.signup.ui.username_en.text()).strip() == '') or ((self.signup.ui.email_en.text()).strip() == '') or ((self.signup.ui.password_en.text()).strip() == '') or ((self.signup.ui.repassword_en.text()).strip() == ''):
                    self.signup.ui.alarmlb.setText('Fill all the blanks') 
                    correct_info = False
                else:
                    # check password
                    numbers = '1234567890'
                    alphabets = 'mnbvcxzasdfghjklpoiuytrewqMNBVCXZASDFGHJKLPOIUYTREWQ'
                    signs = '!@#$%^&*()_-/+'
                    if self.signup.ui.password_en.text() != self.signup.ui.repassword_en.text():
                        self.signup.ui.alarmlb.setText('Passwords are not the same')
                        correct_info = False

                    else:
                        check_pass = [False , False , False]
                        for letter in self.signup.ui.password_en.text():
                            if (letter not in numbers) and (letter not in alphabets) and (letter not in signs):
                                self.signup.ui.alarmlb.setText('Password should contains numbers and alphabets and signs')
                                correct_info = False
                            else:
                                if letter in numbers:
                                    check_pass[0] = True
                                elif letter in alphabets:
                                    check_pass[1] = True
                                elif letter in signs:
                                    check_pass[2] = True
                        
                        if check_pass != [True , True , True]:
                            self.signup.ui.alarmlb.setText('Password should contains numbers and alphabets and signs')
                            correct_info = False
                        else:
                            self.signup.ui.alarmlb.setText('')

                    # check email     
                    try:
                        validate_email(self.signup.ui.email_en.text())

                        cursor.execute("SELECT email FROM acounts;")
                        db_emails = []
                        for email in cursor:
                            db_emails.append(email[0])
                        if self.signup.ui.email_en.text() in db_emails:
                            self.signup.ui.alarmlb.setText('Email already exists')
                            correct_info = False

                    except:
                        self.signup.ui.alarmlb.setText('Email address is not valid')
                        correct_info = False

                    # check username
                    for letter in self.signup.ui.username_en.text():
                        if (letter not in numbers) and (letter not in alphabets) and (letter not in signs):
                            self.signup.ui.alarmlb.setText('Username is not valid')
                            correct_info = False
                        else:
                            cursor.execute("SELECT username FROM acounts;")
                            db_usernames = []
                            for username in cursor:
                                db_usernames.append(username[0])
                            if self.signup.ui.username_en.text() in db_usernames:
                                self.signup.ui.alarmlb.setText('Username already exists')
                                correct_info = False
                            break
                
                # insert infos to database
                if correct_info == True:
                    try:
                        username = self.signup.ui.username_en.text()
                        email = self.signup.ui.email_en.text()
                        password = self.signup.ui.password_en.text()
                        ip = str(socket.gethostname())
                        quary = "INSERT INTO acounts VALUES( \'%s\' , \'%s\' , \'%s\' , \'%s\' , \'%i\' , \'%i\' , \'%i\' , \'%i\' );" % (username , email , password , ip , 0 , 0 , 0 , 0)
                        cursor.execute(quary)
                        connection.commit()

                        self.openMainWindow(username)
                    except:
                        error_msg = QMessageBox()
                        error_msg.setIcon(QMessageBox.Information)
                        error_msg.setText("Someting went wrong")
                        error_msg.setWindowTitle("Error")
                        error_msg.setStandardButtons(QMessageBox.Ok )
                        error_msg.buttonClicked.connect(lambda: error_msg.close())
                        error_msg.exec_()
                    
            


            self.signup.ui.btn_login.clicked.connect(self.logingin)
            self.signup.ui.btn_signup.clicked.connect(putInfoToDB)


        # login page
        self.login.show()
        self.signup.close()
        self.login.ui.btn_signup.clicked.connect(signing)
        self.login.ui.btn_login.clicked.connect(LoginToDB)


    def openMainWindow(self , username):
        self.show()
        self.login.close()
        self.signup.close()

        # open & close sidebar
        def openSidebar():
            geo = self.main.sidebar.geometry()
            if geo == QRect(-180, 0, 180, 620):
                self.anim = QPropertyAnimation(self.main.sidebar , b"geometry")
                self.anim.setDuration(200)
                self.anim.setStartValue(QRect(-180, 0, 180, 620))
                self.anim.setEndValue(QRect(0, 0, 180, 620))
                self.anim.start()
                icon3 = QIcon()
                icon3.addPixmap(QPixmap("%s/img/close-menu.png" % path), QIcon.Normal, QIcon.Off)
                self.main.btn_menu.setIcon(icon3)
                self.main.btn_menu.setIconSize(QSize(30, 30))
            else:
                self.anim = QPropertyAnimation(self.main.sidebar , b"geometry")
                self.anim.setDuration(200)
                self.anim.setStartValue(QRect(0, 0, 180, 620))
                self.anim.setEndValue(QRect(-180, 0, 180, 620))
                self.anim.start()
                icon3 = QIcon()
                icon3.addPixmap(QPixmap("%s/img/menu.png" % path), QIcon.Normal, QIcon.Off)
                self.main.btn_menu.setIcon(icon3)
                self.main.btn_menu.setIconSize(QSize(20, 20))

        # move between pages
        self.main.btn_pageTest.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_type),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }")
        ])
        self.main.btn_pageAcount.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_acount),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }")
        ])
        self.main.btn_pageRanking.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_ranking),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }")
        ])
        self.main.btn_pageCompetitions.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_competitions),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }")
        ])
        self.main.btn_pageSettings.clicked.connect(lambda: [
            self.main.pages.setCurrentWidget(self.main.page_settings),
            self.main.btn_pageSettings.setStyleSheet(" QPushButton { background: #DEDEDE; color: #010A1A; border-radius: 0px; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageAcount.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageRanking.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageCompetitions.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }"),
            self.main.btn_pageTest.setStyleSheet(" QPushButton { background: none; color: #010A1A; } QPushButton:hover {background-color: #DEDEDE;border-radius: 0px; }")
        ])
        # open & close sidebar
        self.main.btn_menu.clicked.connect(openSidebar)

        def TypingTest():
            # set words to type
            import random
            words_toType = ''
            for this in range(350):
                words_toType += str(words[random.randint(0 , len(words)-1)]) + ' '
            words_toType_list = words_toType.split()
            self.main.type_words.setText(words_toType)
            self.main.type_lastword.setText(words_toType_list[0])

            # calculate words
            def typing():
                typed_text = list(self.main.words_en.text())
                print(typed_text)
                if len(typed_text) == 0:
                    typed_text = 'j'

                if typed_text[-1] == ' ':
                    
                    # delete typed word
                    
                    words_toType_list.pop(0)
                    words_toType = ''
                    for word in words_toType_list:
                        words_toType += word + ' '
                    self.main.type_words.setText(words_toType)
                    self.main.type_lastword.setText(words_toType_list[0])
                    self.main.words_en.setText('')
                    

            self.main.words_en.textChanged.connect(typing)
            self.main.words_en.setEnabled(True)
            self.main.words_en.setFocus()

           

        
        self.main.words_en.setEnabled(False)
        self.main.type_restart.clicked.connect(TypingTest)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())
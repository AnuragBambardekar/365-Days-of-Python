# pip install twisted

from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

# Authentication
checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("bamba1","12345")
checker.addUser("bamba2","54321")
checker.addUser("yolo1","54321")

portal = Portal(FTPRealm("213_FTP_server/public","213_FTP_server/myusers"), [AllowAnonymousAccess(), checker])

factory = FTPFactory(portal)

reactor.listenTCP(21, factory)
reactor.run()
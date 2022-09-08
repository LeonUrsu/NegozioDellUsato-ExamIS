import yagmail


yag = yagmail.SMTP('progetto.negozio.is@gmail.com', 'ktvfqnyjuicdpwsz')
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('leoperaz2000@gmail.com', 'subject', contents)
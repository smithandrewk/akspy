def email_after_execution(func):
    print('emailing after execution.')
    def send_mail(send_from, send_to, subject, text, files=None):
        print('sending mail!!')
        import smtplib
        from os.path import basename
        from email.mime.application import MIMEApplication
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.utils import COMMASPACE, formatdate
        assert isinstance(send_to, list)

        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)


        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('andrewsmith1025@gmail.com','billybob99')
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
    import time
    def inner1(*args, **kwargs):
 
        begin = time.time()
         
        func(*args, **kwargs)
 
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

        send_mail('andrewsmith1025@gmail.com',['andrewsmith1025@gmail.com'],subject=f'{func.__name__} execution completed',text=f'Total time taken in : {func.__name__}, {end-begin}')
    return inner1
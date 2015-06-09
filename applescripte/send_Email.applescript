-- this script is set an email template
-- for example:
--      overtime-work email
--
set curDate to do shell script "date +%Y年%m月%d日" 
set recipientAddress to "use your recipientAddress "
set ccAddress to "mail  cc Address "
set bccAddress to "mail  bcc Address "
set theSubject to "mail   Subject "
set theContent to "mail Content "

tell application "Mail"
 
        --Create the message
        set theMessage to make new outgoing message with properties {subject:theSubject, content:theContent, visible:true}
 
        --Set recipients
        tell theMessage
                make new to recipient with properties { address:recipientAddress}
                make new  bcc recipient with properties { address:bccAddress}
                make new  cc recipient with properties { address:ccAddress}
 
                ##Send the Message
				send
 
        end tell
end tell
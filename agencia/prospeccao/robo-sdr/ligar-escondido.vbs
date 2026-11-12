' Robô SDR: roda o iniciar.cmd sem janela preta (o Chrome do WhatsApp continua abrindo normalmente)
Set f = CreateObject("Scripting.FileSystemObject")
Set s = CreateObject("WScript.Shell")
s.CurrentDirectory = f.GetParentFolderName(WScript.ScriptFullName)
s.Run "cmd /c iniciar.cmd", 0, False

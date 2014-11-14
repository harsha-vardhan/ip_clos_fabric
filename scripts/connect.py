from ncclient import manager

def connect(host, port, cmdline, user, password):
        conn = manager.connect(host=host,
        port=port,
        username=user,        
        password=password,
        timeout=10,
        hostkey_verify=False)
        
        result = conn.command(command=cmdline, format='text')
        resultstr = result.tostring
        resultstr = resultstr.splitlines() 
        outputresult = '\n'.join(resultstr)
        return outputresult

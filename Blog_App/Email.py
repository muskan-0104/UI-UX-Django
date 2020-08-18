import requests
def email_alert(first):
    report = {}
    report["value1"] = first
    requests.post("https://maker.ifttt.com/trigger/attendance_alert/with/key/UsRE17bpMUQTdmvvW8lH8oXgxkCI0W4iGxI_6YoCHQ", data=report)

email_alert('Muskan')

    

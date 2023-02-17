def fun(s):
    try:
        user, www = s.split("@")
        web, ext = www.split(".")
        if not user or not web or not ext:
            return False
        return not any([user != "".join(filter(lambda x: x.isalnum() or x in ["_", "-"], user)),
            web != "".join(filter(lambda x: x.isalnum(), web)) , len(ext)>3])
    except:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

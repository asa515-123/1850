# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]


# set comprehension to extract a clean, unique set of lowercase email addresses
clean_setof_emails={i.lower()for i in raw_emails}

# print the clean set of email addressed
print(clean_setof_emails)

# Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).
 
# write another set comprehension for this case to extract a clean, unique set of valid, lowercase email addresses
raw_emails2 = ["UserA@gmail.com","SYSTEM_ALERT","usera@gmail.com","admin@site.com","UserB@yahoo.com"]
clean_setof_emails2={s.lower()for s in raw_emails2 if '@' in s}
print(clean_setof_emails2)
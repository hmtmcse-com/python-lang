# ----------------------------------------------------------------------------------------------------------------------
try:
    print("Main Block")
except:
    print("Something went wrong")
else:
    print("Something else")
finally:
    print("The 'try except' is finished")


# ----------------------------------------------------------------------------------------------------------------------
role = "user"

if role != "admin":
  raise Exception("Restricted area")


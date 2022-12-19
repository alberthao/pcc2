famous_person = "  Albert Einstein \t\n"
saying = "A person who never made a mistake never tried anything new."
message = f'{famous_person.strip()} once said, "{saying}"'
print(message)

message1 = f'{famous_person.lstrip()} once said, "{saying}"'
print(message1)

message2 = f'{famous_person.rstrip()} once said, "{saying}"'
print(message2)
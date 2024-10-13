

key = "A"
key_as_int = int(key, 16) # Use base-16 since we want hex output
key_as_hex = hex(key_as_int)
encrypted_secret = 0x01


decrypted_msg = hex(key_as_int ^ encrypted_secret)
string_decrypted_msg = str(decrypted_msg)

print(decrypted_msg)
print(string_decrypted_msg)



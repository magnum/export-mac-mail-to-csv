
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# assumes your file is called mbox
# writes to a file called mbox.csv

import mailbox
import csv


# handle recursive payloads
# this only exports the human-readable text/plain payload
def more_payloads(message):
	body = ""
	if message.is_multipart():
		for payload in message.get_payload():
			body += more_payloads(payload)
	else:
		if message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
	return body

with open("mbox.csv", "wb") as outfile:
	writer = csv.writer(outfile)

	for message in mailbox.mbox('mbox'): ## 'mbox' needs to match the file you're reading from
		body = more_payloads(message)
		writer.writerow([ message['date'], message['from'], message['subject'],  body])
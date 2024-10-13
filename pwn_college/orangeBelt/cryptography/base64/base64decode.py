import base64

flagEncoded = 'cHduLmNvbGxlZ2V7YzF5bnlPY1B1NEtKZzVuZXUxQnVEcUYzdGdwLmROek56TURMMVlETjBjeld9Cg=='

flag = base64.b64decode(flagEncoded)

print(flag)

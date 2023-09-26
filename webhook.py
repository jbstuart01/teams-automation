import pymsteams

message = pymsteams.connectorcard("https://gtkycu.webhook.office.com/webhookb2/2d3cbdcd-1273-45a9-88cd-08f700236f35@fd352be5-cd5a-411a-b479-71cb930cb5cf/IncomingWebhook/c267d49b29164cd1a4ad169683311853/fdffcb7c-f9c8-49e8-bce1-575c8308b761")

message.title("This message has a title")
message.text("Now I'm in color")
message.color("155680")
message.send()
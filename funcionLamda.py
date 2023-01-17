import json
import os
import mercadopago 


def lambda_handler(event, context):
    #trabajamos con checkoutbrick usando el SDK de mercadopago
    sdk= mercadopago.SDK(os.environ["ACCESS_TOKEN"])

    #event traerá los datos object JSON del cardFormData
    bodyGet = event
    
    #creara el pago
    payment_response = sdk.payment().create(bodyGet)
    payment = payment_response["response"]
    
    #cargara los datos de items.products
    #preference_response = sdk.preference().create(bodyGet["productData"])
    #preference = preference_response["response"]

    #se retorna una respuesta de la generación del pago
    return {
        'statusCode': 200,
        'body': json.dumps(payment)
    }

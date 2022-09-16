class ResponseController:
    
    @staticmethod
    def get_response(status, payload, message=False):
        try:
            body = {}
            body["status"] = status
            body["payload"] = payload
            
            if message:
                body["message"] = message
                
        except:
            body = {}
            
        return body
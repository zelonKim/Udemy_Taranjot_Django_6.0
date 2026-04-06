from django.http import HttpResponse

def CustomFunctionMiddleware(get_response):
    print('🚀 executed when server starts - One time configuration')
    
    def middleware(request):
        print('🔌 executed FM before view is called - Request')
        response = HttpResponse("Response from Function Based Middleware")
        print('💡 executed FM after view is called - Response')
        return response
    
    return middleware





class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('🚀 executed when server starts - One time configuration')
    
    def __call__(self, request):
        print('🔌 executed CM before view is called - Request')
        if(request.path == '/student/get/'):
            print("Get view is Called")
        response = self.get_response(request)
        print('💡 executed CM after view is called - Response')
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("⚡️executed just before calling the view")
        print('요청 메서드:', request.method)
        print('뷰 함수명:', view_func.__name__)
        
    
    def process_exception(self, request, exception):
        print("🚨 executed when exception occured")
        print(exception)
        return HttpResponse("response from process exception")
    
    def process_template_response(self, request, response):
        print('📺 executed just after the TemplateResponse is called')
        response.context_data['context_from_hook'] = '📦 Something from the template hook response'
        return response
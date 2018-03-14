
# API中Validation异常的处理程序
@api.errorhandler(ValidationError):
def validation_error(e):
    return bad_request(e.args[0])


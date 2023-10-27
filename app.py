from tradeadvisor import create_app
from models import * 
from utils import get_logger

logger = get_logger('SMAR')
app = create_app()



@app.route('/test')
def test_api():
    logger.info('Test API is checked!')
    return {'message': "APIs started successfully!"}, 200

if __name__ == "__main__":
    app.run(host='localhost', port='5000')  
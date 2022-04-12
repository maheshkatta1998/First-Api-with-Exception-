import json

from config.config import *
from model.model import *
from model.dealer import *


@app.route('/get_single_record', methods=['GET'])
def getSingleRecord():
    dealer_name = request.args.get('name')
    try:
        dealer_result = session.query(Dealer). \
            filter(Dealer.dealerName == dealer_name).all()
    except Exception as err:
        session.rollback()

    if dealer_result:
        try:
            product_result = session.query(ProductEnquiry). \
                filter(ProductEnquiry.dealerName == dealer_name).all()
            product_result_dict = [item.__dict__ for item in product_result]
            for item in product_result_dict:
                del item['_sa_instance_state']
            return json.dumps(product_result_dict)

        except Exception as err:
            session.rollback()
        finally:
            session.close()

    else:
        return "Unauthorized access"





@app.route('/starts_with', methods=['GET'])
def starts_with_record():
    # dealer_starts = []
    dealer_starts_with = request.args.get('name')
    try:
        dealer_starts = session.query(Dealer).filter(Dealer.dealerName.like(dealer_starts_with + '%')).all()
    except Exception as err:
        session.rollback()
    if dealer_starts:
        try:
            product_starts_with = session.query(ProductEnquiry).filter(
                ProductEnquiry.dealerName.like(dealer_starts_with + '%')).all()
            starts_with_dict = [item.__dict__ for item in product_starts_with]
            for item in starts_with_dict:
                del item['_sa_instance_state']
            return json.dumps(starts_with_dict)
        except Exception as err:
            session.rollback()
        finally:
            session.close()
    else:
        return "Unauthorized access"



# @app.route('/starts', methods=['GET'])
# def starts_with():
#     request_name = request.args.get('name')
#     result = session.query(ProductEnquiry).filter(ProductEnquiry.dealerName.like(request_name + '%')).all()
#     convert_dict = [item.__dict__ for item in result]
#     return str(convert_dict)
#
#
# app.run(debug=False)

@app.route('/ends_with', methods=['GET'])
def ends_with_record():
    dealer_ends_with = request.args.get('name')
    try:
        dealer_ends = session.query(Dealer).filter(
            Dealer.dealerName.like('%' + dealer_ends_with)).all()
    except Exception as err:
        session.rollback()
    if dealer_ends:
        try:
            ends_record = session.query(ProductEnquiry).filter(
                ProductEnquiry.dealerName.like('%' + dealer_ends_with)).all()
            ends_dict = [item.__dict__ for item in ends_record]
            for item in ends_dict:
                del item['_sa_instance_state']
            return json.dumps(ends_dict)
        except Exception as err:
            session.rollback()
        finally:
            session.close()
    else:
        return "Unauthorized access"




@app.route('/contain_records', methods=['GET'])
def Contains_record():
    dealer_contains = request.args.get('name')
    try:
        dealer_contain_record = session.query(Dealer).\
            filter(Dealer.dealerName.like('%'+dealer_contains+'%')).all()
    except Exception as err:
        session.rollback()
    if dealer_contain_record:
        try:
            Contains_dealer = session.query(ProductEnquiry).filter(ProductEnquiry.dealerName.like('%' + dealer_contains +'%')).all()
            contain_result_dict = [item.__dict__ for item in Contains_dealer]
            for item in contain_result_dict:
                del item['_sa_instance_state']
            print("contain_result_dict  --> ", contain_result_dict)
            return jsonify(contain_result_dict)
        except Exception as err:
            session.rollback()
        finally:
            session.close
    else:
        return "Unauthorized access"
app.run(debug=False)
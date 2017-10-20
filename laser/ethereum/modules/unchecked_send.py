from laser.ethereum import utils
import logging

def execute(svm):

    for loc in svm.send_eth_locs:

        node_addr = loc['address']
        function_name = loc['function_name']
        
        logging.info("Investigating Ether send at node " + str(node_addr) + ", function " + function_name)

        models = utils.satisfy(svm, node_addr)

        print("MODELS")
        print(models)
        print("-----")

        i = 1

        if len(models):

            print("Possible Ether send at " + str(node_addr) + ", function " + function_name)

            for model in models:
                print("--- model " + str(i) + " ---")
                for k in model:
                    print(str(k), hex(model[k].as_long()))
                i  += 1
        else:
            logging.info("Investigating Ether send at node " + str(node_addr) + ", function " + function_name)
                

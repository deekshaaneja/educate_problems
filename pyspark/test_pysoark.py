
# 0: location
# 1: spend
# australia, 95

map_spend = {}

def find_spend(input)
    tuple_spend = input.map(lambda input :  input[0], input[1])
    if input[0] in map_spend:
        map_spend[input[0]] += input[1]
    else:
        map_spend[input[0]] = input[1]
#15 mins

# input RDD
sc = Sparksession()

batch_input = sc.textfile(FILEPATH)

spend_rdd = batch.map(lambda batch_input : find_spend(batch_input))

foreachprintln(spend_rdd)
foreachprintln(spend_rdd).top(5)

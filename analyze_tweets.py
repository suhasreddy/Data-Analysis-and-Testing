from textblob import TextBlob
import traceback
import sys

# IMPORTANT !
# Have ony the number of tweets in your tweets.csv file that you can classify at this moment. Like 30, 50 or 100 
# Have new set of tweets each time in your tweets.csv
# Record accuracy displayed at the end also record the number of tweets.
# Your output_classification.csv will conatin the classification information
# send me your accuracy levels along whith corresponding number of tweets and output_classification.csv

fileName = "tweets.csv"

def isExistsURL(tweet):
    '''
    regex obatined from
    http://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
    '''
    urlObject = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)


    if urlObject is None:
        return True
    return False

def WriteToFile(fileName, tweets, myPredict, machinePredict):
    
    f = open('output_classification.csv','a')
    for x in range(0,len(tweets)):
        
        f.write(fileName+","+tweets[x]+","+str(myPredict[x])+","+str(machinePredict[x])+"\n") 
    f.close()


fp= open(fileName, "r")
data = fp.readlines()

fp.close()
user_rows =[]
count=0;
for line in data :
        user_rows.append(line.strip().split(','));
        count = count+1;

tweets=[]
#print count

#print len(user_rows);
for x in range(0,len(user_rows)):
    try:
        if (user_rows[x])[2] not in tweets and len((user_rows[x])[2]) > 0:
            if isNotExistsURL(user_rows[x])[2]:
                print x
                tweets.append((user_rows[x])[2])
            
    except Exception, err:
        pass
               

truth_values = [];
machine_values = [];

x=0;

#print len(user_rows);

#print "tweets"+str(len(tweets))
count = 0;
considered_tweet = []
while(x<len(tweets)-1):
    #print x,tweets[x]

    
    print str(x+1)+"."+tweets[x]
    try:
            response = int(raw_input("Polarity: "));
    except Exception:
        print "*\n Invalid Input\n*";
        continue;

    if response < -1 or response > 1:
        print "*\n Invalid Input\n*";
    else:

        try:
                testimonial = TextBlob(tweets[x])
                machine_prediction= testimonial.sentiment[0]

                if machine_prediction < 0:
                        machine_values.append(-1)

                elif machine_prediction == 0:
                        machine_values.append(0)
        
                elif machine_prediction > 0:
                        machine_values.append(1)

                considered_tweet.append(tweets[x])

                truth_values.append(response);

                print 'Prediction:' + str(machine_values[count])
                count = count+1;
        except Exception, err:

                print err
                print traceback.format_exc()
                print "\n\n **Unrecognized characters in text** \n\n";
        x=x+1;
        
for x in range(0,count):
        print str(x+1)+". "+considered_tweet[x]
        print "\tMy Prediction "+str(truth_values[x])
        print "\tMachine Prediction "+str(machine_values[x])

correct_predictions = 0;
for x in range(0,count):
        if truth_values[x] == machine_values[x]:
                correct_predictions = correct_predictions +1;

print "Number of Tweets Considered " + str(count)
print "Accuracy "+str( float(correct_predictions)*100/count);
        
WriteToFile(fileName, considered_tweet, truth_values, machine_values)

for x in range(0,count):
        if machine_values[x]==1:
            print truth_values[x]

import nltk
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
#input analysis
sent_lambda_parsing_verb=[]
sent_lambda_parsing_subject=[]
sent_lambda_parsing_object=[]
sent_in=[]
sent_txt=[]
end='.'
noun='N'
pronoun='PR'
verb='VB'

#question analysis
question=[]
question_all_word=[]
question_feature=[]
question_feature_verb=[]
question_feature_target=[]
question_feature_determinent=[]
#input analysis function
def input_analysis():
 
 output_file = open('output.txt', 'w') 
 parsesent_file = open('parse_test.txt', 'w')
 f=open('bAb_3.txt','rU')#open the file
 raw=f.read()

#print(raw)

 output_file.write("The sentence of the texts are:"+'\n')

#tokenize the sentence
 token_sent=sent_tokenize(raw)
 a=len(token_sent)
 print('Number of sentences:',a)

#print the sentences
 for i in range(0,a):
  print(token_sent[i])     
 print('\n')

##POS tagging 
 k=0
 for i in range(0,a):
  word_token=nltk.word_tokenize(token_sent[i])
  sent_in.insert(i,token_sent[i])
  
  lngth=len(word_token)
  tag=nltk.pos_tag(word_token)

  #checking tagged words
  for j in range(0,len(tag)):
    if verb in tag[j][1]:
          sent_lambda_parsing_verb.append(tag[j][0])      #verb finding
          for k in range(j+2,len(tag)-1):
            if noun  in tag[k][1]:
             sent_lambda_parsing_object.append(tag[k][0])  #object finding
            elif pronoun in tag[k][1]:
             sent_lambda_parsing_object.append(tag[k][0])    
                
 #finding subject
  for j in range(0,len(tag)):
    if verb not in tag[j][1]:
          sent_lambda_parsing_subject.append(tag[j][0])
    else:
          break

 #print verb, subject, object         
 print('Verb list:',sent_lambda_parsing_verb)   
 print('Subject list:',sent_lambda_parsing_subject)
 print('Object list:',sent_lambda_parsing_object)

print('\n')

#question_analysis fuction
#------------------------------
#--------------------------
def question_analysis():
#input question
 question=input('Enter your question:')
 print(question)
 question_token=nltk.word_tokenize(question)
 print( question_token)
 len_question_token=len(question_token)
 for i in range(0,len_question_token-1):
     question_feature.append(question_token[i])





                

#question answering function 
def answering_question(question_in,verb_in,subj_in,obj_in):

    #some variables
    q_word='W'
    q_noun='NNP'
    q_pronoun='PR'
    q_preposition='IN'
    q_verb='VB'

    len_verb=len(verb_in)
     
    question_attribute=[]
    question_object=[]
    question_preposition=[]
    match=[]
    position_place_checking=[]

    #variables for where analysis
    question_object_word=[]
    question_preposition_word=[]
    question_preposition_object=[]

#positioning
    sent_in=[]
    f=open('positon_verb.txt','rU')#open the file
    position_verb_raw=f.read()
    pos_verb_sentence=sent_tokenize(position_verb_raw)
    word_token_position_verb=nltk.word_tokenize(pos_verb_sentence[0])
        
    sent_in.append(word_token_position_verb)
    len_word_token=len(word_token_position_verb)
    #print(len_word_token)
    print(word_token_position_verb)

    
#place checking
     
    for i in range(0,len(sent_lambda_parsing_verb)):
      count=0
      for j in range(0,len_word_token):
        if sent_lambda_parsing_verb[i]==word_token_position_verb[j]:
             #match.append(word_token_position_verb[j])
          match.append('1')
          print(word_token_position_verb[j])
          break
        elif sent_lambda_parsing_verb[i]!=word_token_position_verb[j]:
             #match.append("N")
          count=count+1
      print('position',i,'is:',count) 
      if count==len_word_token:
           match.append('0')
    print(match)

    
#position of place
        
    for i in range(0,len(sent_lambda_parsing_verb)):
        if '1' in match[i]:
            position_place_checking.append('1')
        elif '1' not in match[i]:
            position_place_checking.append('0')
                
    #print(position_place_checking)           

#carrying verb
    carry_sen_in=[]
    carrying_verb_raw=[]
    carrying_verb_sentence=[]
    word_token_carrying_verb=[]
    match_carry=[]
    position_carry_checking=[]
    
    f1=open('carrying_verb.txt','rU')#open the file
    carrying_verb_raw=f1.read()
    carrying_verb_sentence=sent_tokenize(carrying_verb_raw)
    word_token_carrying_verb=nltk.word_tokenize(carrying_verb_sentence[0])
        
    carry_sen_in.append(word_token_carrying_verb)
    len_carry_sen_in=len(word_token_carrying_verb)
    #print(len_word_token)
    print('Carry verb are :',word_token_carrying_verb)
    
#carry checking
    for i in range(0,len(sent_lambda_parsing_verb)):
      count_carry=0
      for j in range(0,len_carry_sen_in):
        if sent_lambda_parsing_verb[i]==word_token_carrying_verb[j]:
             #match.append(word_token_position_verb[j])
          match_carry.append('1')
          print(word_token_carrying_verb[j])
          break
        elif sent_lambda_parsing_verb[i]!=word_token_carrying_verb[j]:
             #match.append("N")
          count_carry=count_carry+1
      print('position',i,'is:',count_carry)
      
      if count_carry==len_carry_sen_in:
           match_carry.append('0')
    print('Carry position are: ',match_carry)
    
#copying carry to other list
    for i in range(0,len(sent_lambda_parsing_verb)):
        if '1' in match_carry[i]:
            position_carry_checking.append('1')
        elif '1' not in match[i]:
            position_carry_checking.append('0')
   
    #print('Carry position are: ',position_carry_checking)
    

#functions
# question type
    def where_analysis():
        for i in range(0,len_tag_question_list):
            if q_noun==tag_question_list[i][1] or 'NN'==tag_question_list[i][1]:
                question_object_word.append(tag_question_list[i][0])
                print('Noun is:',question_object_word)
            elif q_preposition==tag_question_list[i][1]:
                question_preposition_word.append(tag_question_list[i][0])
      
        print('Questions features are :',question_object_word,question_preposition_word)      
        len_question_object_word=len(question_object_word)
        print(len_question_object_word)

#answering without before/after preposition
        if len_question_object_word==1:
            
          for i in range(len_verb-1,0,-1):
            if question_object_word[0] in subj_in[i]:
              print('Subj',i)
              question_object.append('Sbj')
              subject_position=i
              break
            
            elif question_object_word[0] in obj_in[i]:
              print('Obj',i)
              question_object.append('Obj')
              object_position=i
              break

#answer for the object question
          if  'Obj' in question_object:
           subj_for_obj=sent_lambda_parsing_subject[object_position]
           #print(sent_lambda_parsing_subject)
           print('The subject is :',object_position,subj_for_obj)
           for k in range(object_position-1,0,-1):
            if subj_for_obj==subj_in[k] and position_place_checking[k]=='1':
                print('Answer is:',sent_lambda_parsing_object[k])
                break

#answer for the subject question
          elif 'Sbj' in question_object:
            print('Yes',subject_position)
            subj_for_obj=subj_in[subject_position]  
            #print(position_place_checking)    
        
            for l in range(subject_position,0,-1):
              if subj_for_obj==subj_in[l] and position_place_checking[l]=='1':
                print('Answer is:',sent_lambda_parsing_object[l])
                break
          else:
            print('Answer is not found')

#answering for before/after preposition
#--------------------------------------
#--------------------------------------        
        if len_question_object_word==2:
            print('Yap, 2 input subject')
            
            for i in range(len_verb-1,0,-1):
             if question_object_word[0] in subj_in[i]:
              print('Subj',i)
              question_object.append('Sbj_1')
              subject_position_first=i
              break
            
             elif question_object_word[0] in obj_in[i]:
              print('Obj',i)
              question_object.append('Obj_1')
              object_position_first=i
              break
            for i in range(len_verb-1,0,-1):
              if question_object_word[1] in subj_in[i]:
               subject_position_second=i
               question_object.append('Sbj_2')
               break
              elif question_object_word[1] in obj_in[i]:
               object_position_second=i
               question_object.append('Obj_2')
               break
              
            print(question_object)
            
#answering for object question            
            if  'Obj_1' in question_object[0] and 'Sbj_2' in question_object[1]:
             subj_for_obj=sent_lambda_parsing_subject[object_position_first]
           #print(sent_lambda_parsing_subject)
             print('The subject is :',object_position_first,subj_for_obj)
             
             for k in range(subject_position_second-1,0,-1):
              if subj_for_obj==subj_in[k] and position_place_checking[k]=='1':
                print('Answer is:',k,'th position',sent_lambda_parsing_object[k])
                #break
            
            elif 'Obj_1' in question_object[0] and 'Obj_2' in question_object[1]:
                
             subj_for_obj_1=sent_lambda_parsing_subject[object_position_first]
             obj2_for_obj_1=sent_lambda_parsing_object[object_position_second]
             #print(sent_lambda_parsing_subject)
             print('The object is :',object_position_second,obj2_for_obj_1)
             print('The subject is :',object_position_first,subj_for_obj_1)
             
             for k in range(object_position_second-1,0,-1):
              if subj_for_obj_1==subj_in[k] and position_place_checking[k]=='1':
                print('Answer is:',k,'th position',sent_lambda_parsing_object[k])
                #break
            
#answering for subject in first in the question
            #subj + Subj in question
            elif 'Sbj_1' in question_object[0] and 'Sbj_2' in question_object[1]:
             subj_for_subj_1=sent_lambda_parsing_subject[subject_position_first]
            
             subj_for_subj_2=sent_lambda_parsing_subject[subject_position_second]
             #print(sent_lambda_parsing_subject)
             
             for k in range(subject_position_second-1,0,-1):
              if subj_for_subj_1==subj_in[k] and position_place_checking[k]=='1':
                print('Answer is:',k,'th position: ',sent_lambda_parsing_object[k])
                #break


            #Subj+ Obj in question
                
            elif 'Sbj_1' in question_object[0] and 'Obj_2' in question_object[1]:
             subj_for_subj_1=sent_lambda_parsing_subject[subject_position_first]
            
             obj_for_subj_2=sent_lambda_parsing_object[object_position_second]
             #print(sent_lambda_parsing_subject)
             
             for k in range(object_position_second-1,0,-1):
              if subj_for_subj_1==subj_in[k] and position_place_checking[k]=='1':
                print('Answer is:',k,'th position: ',sent_lambda_parsing_object[k])
                #break
            else:
                print('Answer is not found')
                

#YES_NO question answering
    def is_analysis():
        #print('Yes/No')
        for i in range(0,len_tag_question_list):
            if q_noun==tag_question_list[i][1] or 'NN'==tag_question_list[i][1]:
                question_object_word.append(tag_question_list[i][0])

        print(question_object_word)
        subj_for_question=question_object_word[0]
        obj_for_question =question_object_word[1]

        for i in range(len_verb-1,0,-1):
             if subj_for_question in subj_in[i]:
              print('Subj',i)
              #question_object.append('Sbj_1')
              subject_position=i
              break
        for i in range(len_verb-1,0,-1):
             if obj_for_question in obj_in[i]:
              print('Obj',i)
              #question_object.append('Sbj_1')
              object_position=i
              break
            
#answering question
        count_for_no=0    
        for k in range(subject_position,0,-1):
             #if subj_for_question==subj_in[k] and position_place_checking[k]=='1' and obj_for_question==obj_in[k]:
              if subj_for_question==subj_in[k] and position_place_checking[k]=='1' and obj_for_question==obj_in[k]:
              
                print('Answer is:',k,'th position: ','Yes')
                count_for_no=count_for_no+1
                #break
            
        if(count_for_no==0):
            print('No')

             
                 
               
       
#the question started with what 
    def what_analysis():
        what_question_subject=[]
        
        for i in range(0,len_tag_question_list):
            if q_noun==tag_question_list[i][1] or 'NN'==tag_question_list[i][1] or q_verb in tag_question_list[i][1]:
                question_object_word.append(tag_question_list[i][0])

        print(question_object_word)

        what_question_subject=question_object_word[1]

        count_carry_answer=0
        for k in range(len_verb-1,0,-1):
              if what_question_subject==subj_in[k] and match_carry[k]=='1':
                print('Answer is:',k,'th position: ',sent_lambda_parsing_object[k])
                count_carry_answer=count_carry_answer+1
        
        if(count_carry_answer==0):
          print('No answer found')
        
        
#question veryfying here     
    
    question_list=question_in
    print("Question is :",question_list)
    tag_question_list=nltk.pos_tag(question_list)
    len_tag_question_list=len(tag_question_list)
    for i in range(0,len_tag_question_list):
        print(tag_question_list[i][0],'......',tag_question_list[i][1])

    question_attribute=tag_question_list[0][0]
    print(question_attribute)
    if q_word in tag_question_list[0][1] or q_verb in tag_question_list[0][1]:
        
        print('Question is ok')

        if question_attribute=='Where':
            where_analysis()
                
                
        elif question_attribute=='What':
            what_analysis()
                
        elif question_attribute=='Is':
            is_analysis()
        
    else: 
        print('Wrong Question/ Unable to answer')
       

   
#main function is defined here    

def main():
    input_analysis()
    question_analysis()
    answering_question(question_feature,sent_lambda_parsing_verb,sent_lambda_parsing_subject,sent_lambda_parsing_object)
    
main()
 

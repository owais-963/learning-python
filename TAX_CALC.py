def tax_calculator():
    tax_slabes=pd.read_html("https://taxsummaries.pwc.com/pakistan/individual/taxes-on-personal-income")[1]
    c1=np.array(list(tax_slabes[0][2:14]))
    c2=np.array(list(tax_slabes[1][2:14]))
    c3=np.array(list(tax_slabes[2][2:14]))
    c4=np.array(list(tax_slabes[3][2:14]))
    c1=c1.astype('float64')
    c2=np.where(c2=='nan',mt.inf,c2).astype('float64')
    c3=np.where(c3=='nan',0,c3).astype('float64')
    c4=np.where(c4=='nan','0%',c4).astype('str')
    data={'Income_Over':c1,'Income_Not_Over':c2,'Tax_on_first_column_PKR':c3,'Percentage_on_excess':c4}
    tax_slabes=pd.DataFrame(data)
    income=input("Enter your income: ")
    try:
        income=int(income)
        if income>=0:
            ind1=np.where(income>=tax_slabes.Income_Over)
            ind2=np.where(income<tax_slabes.Income_Not_Over)
            ind=np.intersect1d(ind1,ind2)
            if(len(ind)==1):
                ind=ind[0]
                tax_label=tax_slabes.filter(items=[ind],axis=0)
                per_exced=tax_label.Percentage_on_excess[ind]
                per_exced=float(per_exced[0:len(per_exced)-1])
                tax_of_column_one=tax_label.Tax_on_first_column_PKR[ind]
                if ind!=0:
                    income=income-tax_label.Income_Over[ind]
                tax_apply=income/100*per_exced+tax_of_column_one
                return print(f"The Amount of Tax which you have to pay is {tax_apply}") , display(tax_label)
            elif (len(ind)<1):
                return print("length of index is less than 1")
            else:
                return print('length of index is excede from 1')
        else:
            return print("Income is must be greater than 0")
    except Exception as e:
        if type(e)==ValueError:
            input_type=type(income)
            if input_type==str:
                print("Please Enter a number not a string")
            else:
                print(f"{input_type} is not valid or contact to the service provider")
        else:
            print(f"Exception {e} occourd please contact to the service provider")
    finally:
        display(tax_slabes)
        

if __name__=="__main__":
    tax_calculator()
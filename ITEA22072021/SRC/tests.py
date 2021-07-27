from main import sum_numbers
def test_sum_numbers():
    """
    --type mismatch
    --return type mismatch
    --return correct values
    """
    a=1
    b=2
    c=100500

    result=sum_numbers(a,b,c)

    #if result !=100503:
   #     print(f"fail: {result}!=100503")
    assert result==100503
if __name__ =='__main__':
    test_sum_numbers()


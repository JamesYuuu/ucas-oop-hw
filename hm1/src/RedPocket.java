import java.util.Random;
import java.util.Scanner;

public class RedPocket
{
    float money;
    int people;
    public RedPocket(float money,int people)
    {
        this.money=money;
        this.people=people;
    }
    public void calculate()
    {
        Random r=new Random();
        int currentMoney=(int)(money*100);
        int currentPeople=this.people;
        for (int i=1;i<people;i++)
        {
            //确保每次分发的包最多不超过余下所要分发平均数的2倍
            int moneyToGive=r.nextInt(currentMoney/currentPeople*2);
            currentMoney-=moneyToGive;
            currentPeople--;
            System.out.println("Person "+i+" gets "+String.format("%.2f",moneyToGive/100.0f)+" yuan");
        }
        System.out.println("Person "+people+" gets "+String.format("%.2f",currentMoney/100.0f)+" yuan");
    }
    public static void main(String[] args)
    {
        Scanner input=new Scanner(System.in);
        float money= input.nextFloat();
        int people= input.nextInt();
        RedPocket rp=new RedPocket(money,people);
        rp.calculate();
    }
}
import java.util.HashSet;
public class CallCenter {
  
  private HashSet<Employee> employees;
  private TL tl;
  private PM pm;
  public CallCenter(){
    int id;
    for (id = 0; id < 5; id++){
      employees.add(new Employee(id));
    }
    tl = new TL(id++);
    pm = new PM(id);

  }
  
  public void getCallHandler(){
  }


}

public class Employee {

  private int id;
  private boolean busy = False;

  public Employee(int id){
    this.id = id; //TODO: should the id be a constructor argument? How do i autogenerate IDs?
  }

  public int getId(){
    return this.id;
  }

  public boolean handleCall(){
    if (busy){
      return False;
    } else{
      this.busy = True;
      return True;
    }
  }

  protected void endCall(){
    this.busy = False;
  }

}

public class TL extends Employee {

  public TL(int id){
    super(int);
  }
}

public class PM extends Employee {

  public TL(int id){
    super(int);
  }
}

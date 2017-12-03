using System;

public static class Util
{
  public static void CheckAnswer<I, O>(I spreadsheet, Func<I, O> calculator, O expectedOutput)
  {
    O actualOutput = calculator(spreadsheet);

    if (actualOutput.Equals(expectedOutput))
    {
      Console.WriteLine($"Case success!");
    }
    else
    {
      Console.WriteLine($"Case FAILED. Expected {expectedOutput} but got {actualOutput}.");
    }
  }
}

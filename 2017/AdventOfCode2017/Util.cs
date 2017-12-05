using System;

public static class Util
{
  public static void CheckAnswer<I, O>(I input, Func<I, O> calculator, O expectedOutput)
  {
    O actualOutput = calculator(input);

    if (actualOutput.Equals(expectedOutput))
    {
      Console.WriteLine($"Case success!");
    }
    else
    {
      Console.WriteLine($"Case FAILED. Expected {expectedOutput} but got {actualOutput}.");
    }
  }

  public static string GetFileContents(string fileName)
  {
    return System.IO.File.ReadAllText($"../../{fileName}.txt");
  }

  public static string[] GetFileLines(string fileName)
  {
    return System.IO.File.ReadAllLines($"../../{fileName}.txt");
  }

  public static void PrintOutputFromFile<I, O>(string fileName, Func<string, O> calculator)
  {
    Console.WriteLine(calculator(GetFileContents(fileName)));
  }
}

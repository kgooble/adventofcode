using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode2017
{
  class Day2
  {
    public static void Main(string[] args)
    {
      CheckAnswer("5 1 9 5\n7 5 3  \n2 4 6 8", CalculateChecksum, 18);
      CheckAnswer("5 9 2 8\n9 4 7 3\n3 8 6 5", EvenlyDivisibleChecksum, 9);

      string spreadsheet = System.IO.File.ReadAllText("../../Day2.txt");

      Console.WriteLine($"Part 1 solution: {CalculateChecksum(spreadsheet)}");
      Console.WriteLine($"Part 2 solution: {EvenlyDivisibleChecksum(spreadsheet)}");

      Console.ReadKey();
    } 

    private static int EvenlyDivisibleChecksum(string spreadsheet)
    {
      string[] lines = spreadsheet.Split('\n');
      int checksum = 0;
      var numberRows = new List<IEnumerable<int>>();

      foreach (string line in lines)
      {
        string[] numberStrings = line.Split();

        IEnumerable<int> numberRow =
          from numberString in numberStrings
          where !string.IsNullOrWhiteSpace(numberString)
          select int.Parse(numberString);

        numberRows.Add(numberRow);
      }

      foreach (IEnumerable<int> numberRow in numberRows) 
      {
        foreach (int number in numberRow)
        {
          foreach (int otherNumber in numberRow)
          {
            if (number != otherNumber && number % otherNumber == 0)
            {
              checksum += number / otherNumber;
            }
          }
        }
      }

      return checksum;
    }

    private static int CalculateChecksum(string spreadsheet)
    {
      string[] lines = spreadsheet.Split('\n');

      int checksum = 0;
      foreach (string line in lines)
      {
        string[] numberStrings = line.Split();
        IEnumerable<int> numbers = from s in numberStrings
                                   where !string.IsNullOrWhiteSpace(s)
                                   select int.Parse(s);

        int min = numbers.Min();
        int max = numbers.Max();

        checksum += max - min;
      }

      return checksum;
    }

    private static void CheckAnswer(string spreadsheet, Func<string, int> calculator, int expectedChecksum)
    {
      int actualChecksum = calculator(spreadsheet);

      if (actualChecksum == expectedChecksum)
      {
        Console.WriteLine($"Checksum success!");
      }
      else
      {
        Console.WriteLine($"Sequence FAILED. Expected {expectedChecksum} but got {actualChecksum}.");
      }
    }
  }
}

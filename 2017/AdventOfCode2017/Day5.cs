using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2017
{
  class Day5
  {
    public static void Main(string[] args)
    {
      Util.CheckAnswer("0 3  0  1 -3".Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries), NumStepsToExit, 5);

      Part1();

      Util.CheckAnswer("0 3  0  1 -3".Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries), FunkyNumStepsToExit, 10);

      Part2();

      Console.ReadKey();
    }

    private static void Part1()
    {
      Console.WriteLine(NumStepsToExit(Util.GetFileLines("Day5")));
    }

    private static void Part2()
    {
      Console.WriteLine(FunkyNumStepsToExit(Util.GetFileLines("Day5")));
    }

    private static int NumStepsToExit(IEnumerable<string> rawInstructions)
    {
      List<int> jumpValues = new List<int>(rawInstructions.Select(rawInstruction => int.Parse(rawInstruction)));

      int numSteps = 0;
      int index = 0;

      while (index >= 0 && index < jumpValues.Count)
      {
        int oldIndex = index;
        index += jumpValues[index];
        jumpValues[oldIndex]++;
        numSteps++;
      }

      return numSteps;
    }

    private static int FunkyNumStepsToExit(IEnumerable<string> rawInstructions)
    {
      List<int> jumpValues = new List<int>(rawInstructions.Select(rawInstruction => int.Parse(rawInstruction)));

      int numSteps = 0;
      int index = 0;

      while (index >= 0 && index < jumpValues.Count)
      {
        int oldIndex = index;

        index += jumpValues[index];

        if (jumpValues[oldIndex] >= 3)
        {
          jumpValues[oldIndex]--;
        }
        else
        {
          jumpValues[oldIndex]++;
        }

        numSteps++;
      }

      return numSteps;
    }
  }
}

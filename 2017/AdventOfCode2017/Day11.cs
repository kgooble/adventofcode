using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2017
{
  class Day11
  {
    public static void Main(string[] args)
    {
      Util.CheckAnswer(new[] { "ne", "ne", "ne" }, s => FindShortestPath(s, out int maxSteps), 3);
      Util.CheckAnswer(new[] { "ne", "ne", "sw", "sw" }, s => FindShortestPath(s, out int maxSteps), 0);
      Util.CheckAnswer(new[] { "ne", "ne", "s", "s" }, s => FindShortestPath(s, out int maxSteps), 2);
      Util.CheckAnswer(new[] { "se", "sw", "se", "sw", "sw" }, s => FindShortestPath(s, out int maxSteps), 3);

      IEnumerable<string> steps = Util.GetFileContents("Day11").Split(new[] { "," }, StringSplitOptions.RemoveEmptyEntries);

      Part1(steps);

      Part2(steps);

      Console.ReadKey();
    }

    private static void Part1(IEnumerable<string> steps)
    {
      Console.WriteLine(FindShortestPath(steps, out int maxSteps));
    }

    private static void Part2(IEnumerable<string> steps)
    {
      FindShortestPath(steps, out int maxSteps);
      Console.WriteLine(maxSteps);
    }

    private static int FindShortestPath(IEnumerable<string> steps, out int maxSteps)
    {
      maxSteps = 0;
      Dictionary<string, int> bestPath = new Dictionary<string, int>();

      foreach (string step in steps)
      {
        if (bestPath.ContainsKey(Opposite(step)))
        {
          Deduct(bestPath, Opposite(step));
          continue;
        }

        bool canceled = false;
        IEnumerable<string> lateralOpposites = LateralOpposites(step);
        foreach (string opposite in lateralOpposites)
        {
          if (bestPath.ContainsKey(opposite))
          {
            Deduct(bestPath, opposite);
            Add(bestPath, Midpoint(step, opposite));
            canceled = true;
            break;
          }
        }

        if (!canceled)
        {
          Add(bestPath, step);
          maxSteps = Math.Max(maxSteps, bestPath.Values.Sum());
        }
      }

      return bestPath.Values.Sum();
    }

    private static void Deduct(Dictionary<string, int> steps, string key)
    {
      steps[key]--;
      if (steps[key] == 0)
      {
        steps.Remove(key);
      }
    }

    private static void Add(Dictionary<string, int> steps, string key)
    {
      int current;
      steps.TryGetValue(key, out current);
      steps[key] = current + 1;
    }

    private static IEnumerable<string> LateralOpposites(string dir)
    {
      switch (dir)
      {
        case "ne":
          return new[] { "s", "nw" };
        case "nw":
          return new[] { "ne", "s" };
        case "se":
          return new[] { "sw", "n" };
        case "sw":
          return new[] { "se", "n" };
        case "s":
          return new[] { "ne", "nw" };
        case "n":
          return new[] { "sw", "se" };
      }

      return new string[0];
    }

    private static string Midpoint(string dir, string opposite)
    {
      if (dir.Length == 1)
      {
        return dir + opposite[1];
      }

      if (opposite.Length == 1)
      {
        return opposite + dir[1];
      }

      return opposite.Substring(0, 1);
    }

    private static string Opposite(string dir)
    {
      switch (dir)
      {
        case "n":
          return "s";
        case "s":
          return "n";
        case "se":
          return "nw";
        case "nw":
          return "se";
        case "sw":
          return "ne";
        case "ne":
          return "sw";
      }

      throw new ArgumentException($"Unexpected direction {dir}; no opposite found");
    }
  }
}

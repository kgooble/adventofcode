using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode2017
{
  class Day13
  {
    public static void Main(string[] args)
    {
      Util.CheckAnswer(0, t => CalculatePosition(t, 3), 0);
      Util.CheckAnswer(1, t => CalculatePosition(t, 3), 1);
      Util.CheckAnswer(2, t => CalculatePosition(t, 3), 2);
      Util.CheckAnswer(3, t => CalculatePosition(t, 3), 1);
      Util.CheckAnswer(4, t => CalculatePosition(t, 3), 0);

      Util.CheckAnswer(0, t => CalculatePosition(t, 4), 0);
      Util.CheckAnswer(1, t => CalculatePosition(t, 4), 1);
      Util.CheckAnswer(2, t => CalculatePosition(t, 4), 2);
      Util.CheckAnswer(3, t => CalculatePosition(t, 4), 3);
      Util.CheckAnswer(4, t => CalculatePosition(t, 4), 2);
      Util.CheckAnswer(5, t => CalculatePosition(t, 4), 1);
      Util.CheckAnswer(6, t => CalculatePosition(t, 4), 0);

      Util.CheckAnswer(34, t => CalculatePosition(t, 18), 0);
      Util.CheckAnswer(17, t => CalculatePosition(t, 18), 17);

      Util.CheckAnswer(30, t => CalculatePosition(t, 8), 2);

      var input = new string[]
      {
        "0: 3",
        "1: 2",
        "4: 4",
        "6: 4"
      };

      Util.CheckAnswer(input, CalculateSeverity, 24);

      Console.WriteLine("-----------");
      Console.WriteLine(CalculateSeverity(Util.GetFileLines("Day13")));

      Util.CheckAnswer(input, CalculateSeconds, 10);
      Console.WriteLine(CalculateSeconds(Util.GetFileLines("Day13")));

      Console.ReadKey();
    }

    private static int CalculateSeconds(string[] input)
    {
      int i = 0;
      while (true)
      {
        if (i > 30000000)
        {
          break;
        }

        CalculateSeverity(input, i, out int timesCaught);
        if (timesCaught == 0)
        {
          return i;
        }

        i++;
      }

      throw new Exception("couldn't find answer after a lot of tries");
    }

    private static int CalculateSeverity(string[] input)
    {
      return CalculateSeverity(input, 0, out int beans);
    }

    private static int CalculateSeverity(string[] input, int initialDelay, out int timesCaught)
    {
      Dictionary<int, int> scannerInfo = GetScannerInfo(input);

      timesCaught = 0;
      int severity = 0;

      foreach (KeyValuePair<int, int> layerToDepth in scannerInfo)
      {
        int range = layerToDepth.Value;
        int layer = layerToDepth.Key;
        int curPosition = CalculatePosition(layer + initialDelay, range);
        if (curPosition == 0)
        {
          severity += layer * range;
          timesCaught++;
        }
      }

      return severity;
    }

    private static int CalculatePosition(int picosecond, int range)
    {
      if (range % 2 == 0)
      {
        int doubleThing = ((range - 1) * 2);
        int t = picosecond % doubleThing;

        if (t >= range)
        {
          return doubleThing - t;
        }

        return t;
      }
      else
      {
        int doubleThing = range * 2 - 2;
        int t = picosecond % doubleThing;

        if (t >= range)
        {
          return doubleThing - t;
        }

        return t;
      }

      throw new Exception("unexpected");
    }

    private static Dictionary<int, int> GetScannerInfo(string[] input)
    {
      var scannerInfo = new Dictionary<int, int>();

      foreach (string depthRange in input)
      {
        string[] values = depthRange.Split(new[] { ": " }, StringSplitOptions.RemoveEmptyEntries);
        int depth = int.Parse(values[0]);
        int range = int.Parse(values[1]);
        scannerInfo[depth] = range;
      }

      return scannerInfo;
    }
  }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2017
{
  class Day10
  {
    private const string INPUT = "70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41";

    public static void Main(string[] args)
    {
      Util.CheckAnswer(new[] { 0, 1, 2, 3, 4 }, array => string.Join(",", Reverse(array, 0, 3)), "2,1,0,3,4");
      Util.CheckAnswer(new[] { 2, 1, 0, 3, 4 }, array => string.Join(",", Reverse(array, 3, 4)), "4,3,0,1,2");

      Util.CheckAnswer(new[] { 0, 1, 2, 3, 4 }, array => KnotHashRound(array, new[] { 3, 4, 1, 5 }), 12);

      Part1();

      Util.CheckAnswer("1,2,3", str => string.Join(",", DetermineLengths(str)), "49,44,50,44,51,17,31,73,47,23");

      Util.CheckAnswer("", str => KnotHash(str), "a2582a3a0e66e6e86e3812dcb672a272");
      Util.CheckAnswer("AoC 2017", str => KnotHash(str), "33efeb34ea91902bb2f59c9920caa6cd");
      Util.CheckAnswer("1,2,3", str => KnotHash(str), "3efbe78a8d82f29979031a4aa0b16a9d");

      Part2();

      Console.ReadKey();
    }

    private static void Part1()
    {
      IEnumerable<int> lengths =
        INPUT.Split(new[] { ',' }, StringSplitOptions.RemoveEmptyEntries).Select(s => int.Parse(s));

      Console.WriteLine(KnotHashRound(CreateArray(), lengths));
    }

    private static void Part2()
    {
      Console.WriteLine(KnotHash(INPUT));
    }

    private static string KnotHash(string ascii, int totalRounds = 64)
    {
      int[] array = CreateArray();
      int currentPosition = 0;
      int skipSize = 0;
      IEnumerable<int> lengths = DetermineLengths(ascii);
      int[] sparseHash = CreateArray();

      for (int i = 0; i < totalRounds; i++)
      {
        foreach (int length in lengths)
        {
          sparseHash = Reverse(sparseHash, currentPosition, length);
          currentPosition += length + skipSize;
          skipSize++;
        }
      }

      string[] denseHash = new string[16];
      for (int i = 0; i < 16; i++)
      {
        int result = sparseHash[i * denseHash.Length];
        for (int j = 1; j < 16; j++)
        {
          result ^= sparseHash[i * denseHash.Length + j];
        }

        denseHash[i] = result.ToString("X");

        if (denseHash[i].Length == 1)
        {
          denseHash[i] = "0" + denseHash[i];
        }
      }

      return string.Join("", denseHash).ToLower();
    }

    private static IEnumerable<int> DetermineLengths(string str)
    {
      IEnumerable<int> intsFromStr = Encoding.ASCII.GetBytes(str).Select(b => int.Parse(b.ToString()));
      List<int> allLengths = new List<int>(intsFromStr);
      allLengths.AddRange(new[] { 17, 31, 73, 47, 23 });
      return allLengths;
    }

    private static int[] CreateArray(int length = 256)
    {
      int[] array = new int[length];

      for (int i = 0; i < array.Length; i++)
      {
        array[i] = i;
      }

      return array;
    }

    private static int KnotHashRound(int[] initialArray, IEnumerable<int> lengths)
    {
      int currentPosition = 0;
      int skipSize = 0;

      foreach (int length in lengths)
      {
        initialArray = Reverse(initialArray, currentPosition, length);
        currentPosition += length + skipSize;
        skipSize++;
      }

      return initialArray[0] * initialArray[1];
    }

    private static T[] Reverse<T>(T[] array, int startPosition, int length)
    {
      var oldValues = new List<T>(length);

      for (int i = 0; i < length; i++)
      {
        oldValues.Add(array[GetWrappedIndex(i + startPosition, array.Length)]);
      }

      oldValues.Reverse();

      for (int i = 0; i < length; i++)
      {
        array[GetWrappedIndex(i + startPosition, array.Length)] = oldValues[i];
      }

      return array;
    }

    private static int GetWrappedIndex(int index, int length)
    {
      return index % length;
    }
  }
}

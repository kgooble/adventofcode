using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode2017
{
  class Day4
  {
    public static void Main(string[] args)
    {
      Util.CheckAnswer("aa bb cc dd ee", IsValid, true);
      Util.CheckAnswer("aa bb cc dd aa", IsValid, false);
      Util.CheckAnswer("aa bb cc dd aaa", IsValid, true);

      Part1();

      Util.CheckAnswer("abcde fghij", IsValidWithAnagrams, true);
      Util.CheckAnswer("abcde xyz ecdab", IsValidWithAnagrams, false);
      Util.CheckAnswer("a ab abc abd abf abj", IsValidWithAnagrams, true);
      Util.CheckAnswer("iiii oiii ooii oooi oooo", IsValidWithAnagrams, true);
      Util.CheckAnswer("oiii ioii iioi iiio", IsValidWithAnagrams, false);

      Part2();

      Console.ReadKey();
    }

    private static void Part1()
    {
      string[] passPhrases = Util.GetFileLines("Day4");
      Console.WriteLine($"Valid passphrase count: {CountValidPassphrases(passPhrases, IsValid)}");
    }

    private static void Part2()
    {
      string[] passPhrases = Util.GetFileLines("Day4");
      Console.WriteLine($"Valid passphrase count: {CountValidPassphrases(passPhrases, IsValidWithAnagrams)}");
    }

    private static int CountValidPassphrases(IEnumerable<string> passPhrases, Func<string, bool> validityChecker)
    {
      return passPhrases.Count(p => validityChecker(p));
    }

    private static bool IsValid(string passphrase)
    {
      string[] words = passphrase.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
      ISet<string> set = new HashSet<string>(words);
      return set.Count == words.Length;
    }

    private static bool IsValidWithAnagrams(string passphrase)
    {
      string[] words = passphrase.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

      var characterCounts = new List<Dictionary<char, int>>(words.Select(CharacterCounts));

      for (int i = 0; i < characterCounts.Count; i++)
      {
        for (int j = i + 1; j < characterCounts.Count; j++)
        {
          if (Equivalent(characterCounts[i], characterCounts[j]))
          {
            return false;
          }
        }
      }

      return true;
    }

    private static Dictionary<char, int> CharacterCounts(string word)
    {
      var dict = new Dictionary<char, int>();

      return word.GroupBy(c => c).ToDictionary(group => group.Key, group => group.Count());
    }

    private static bool Equivalent(Dictionary<char, int> dict1, Dictionary<char, int> dict2)
    {
      if (dict1.Count != dict2.Count)
      {
        return false;
      }

      foreach (var kvp in dict1)
      {
        if (!dict2.ContainsKey(kvp.Key) || dict2[kvp.Key] != kvp.Value)
        {
          return false;
        }
      }

      return true;
    }
  }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace AdventOfCode2017
{
  class Day8
  {
    private const string INSTRUCTION_PATTERN = @"^(\w+) (inc|dec) (-?\d+) if (\w+) (>|<|>=|<=|!=|==) (-?\d+)$";
    private const int REGISTER_TO_MODIFY_INDEX = 1;
    private const int MODIFICATION_OPERATOR_INDEX = 2;
    private const int MODIFICATION_AMOUNT_INDEX = 3;
    private const int CONDITION_REGISTER_INDEX = 4;
    private const int CONDITION_OPERATOR_INDEX = 5;
    private const int CONDITION_OPERAND_INDEX = 6;

    public static void Main(string[] args)
    {
      string[] sampleInput = new[] {
        "b inc 5 if a > 1",
        "a inc 1 if b < 5",
        "c dec -10 if a >= 1",
        "c inc -20 if c == 10"
      };

      Util.CheckAnswer(
        sampleInput,
        FindLargestValue,
        1);

      Part1();

      Util.CheckAnswer(
        sampleInput,
        FindLargestValueAtAnyTime,
        10);

      Part2();

      Console.ReadKey();
    }

    private static void Part1()
    {
      Console.WriteLine(FindLargestValue(Util.GetFileLines("Day8")));
    }

    private static void Part2()
    {
      Console.WriteLine(FindLargestValueAtAnyTime(Util.GetFileLines("Day8")));
    }

    private static int FindLargestValue(IEnumerable<string> rawInstructions)
    {
      var registers = new Dictionary<string, int>();

      foreach (string rawInstruction in rawInstructions)
      {
        Instruction instr = CreateInstruction(rawInstruction);
        instr.Apply(registers);
      }

      return registers.Values.Max();
    }

    private static int FindLargestValueAtAnyTime(IEnumerable<string> rawInstructions)
    {
      var registers = new Dictionary<string, int>();
      int maxValue = int.MinValue;

      foreach (string rawInstruction in rawInstructions)
      {
        Instruction instr = CreateInstruction(rawInstruction);
        int newValue = instr.Apply(registers);
        maxValue = Math.Max(newValue, maxValue);
      }

      return maxValue;
    }

    private static Instruction CreateInstruction(string rawInstruction)
    {
      Regex rgx = new Regex(INSTRUCTION_PATTERN, RegexOptions.IgnoreCase);
      Match match = rgx.Match(rawInstruction);

      if (match == null)
      {
        throw new ArgumentException($"Could not match instruction '{rawInstruction}'");
      }

      return new Instruction(
        match.Groups[REGISTER_TO_MODIFY_INDEX].Value,
        CreateModifier(match.Groups[MODIFICATION_OPERATOR_INDEX].Value),
        int.Parse(match.Groups[MODIFICATION_AMOUNT_INDEX].Value),
        match.Groups[CONDITION_REGISTER_INDEX].Value,
        CreateOperator(match.Groups[CONDITION_OPERATOR_INDEX].Value),
        int.Parse(match.Groups[CONDITION_OPERAND_INDEX].Value));
    }

    private static Modifier CreateModifier(string rawModifier)
    {
      if (rawModifier == "inc")
      {
        return Modifier.Inc;
      }

      return Modifier.Dec;
    }

    private static Operator CreateOperator(string rawOperator)
    {
      switch (rawOperator)
      {
        case ">=":
          return Operator.GreaterOrEqual;
        case ">":
          return Operator.Greater;
        case "<":
          return Operator.Less;
        case "<=":
          return Operator.LessOrEqual;
        case "==":
          return Operator.Equal;
        case "!=":
          return Operator.NotEqual;
      }

      throw new ArgumentException($"Could not parse raw operator '{rawOperator}'");
    }

    private enum Modifier
    {
      Inc,
      Dec
    }

    private enum Operator
    {
      Greater,
      GreaterOrEqual,
      Less,
      LessOrEqual,
      Equal,
      NotEqual
    }

    private struct Instruction
    {
      public readonly string registerToModify;
      public readonly Modifier modifier;
      public readonly int modificationAmount;
      public readonly string conditionRegister;
      public readonly Operator conditionOperator;
      public readonly int conditionOperand;

      public Instruction(
        string registerToModify,
        Modifier mod,
        int modAmount,
        string conditionRegister,
        Operator conditionOperator,
        int conditionOperand)
      {
        this.registerToModify = registerToModify;
        this.modifier = mod;
        this.modificationAmount = modAmount;
        this.conditionRegister = conditionRegister;
        this.conditionOperator = conditionOperator;
        this.conditionOperand = conditionOperand;
      }

      public int Apply(Dictionary<string, int> registers)
      {
        registers.TryGetValue(this.conditionRegister, out int conditionRegisterCurrentValue);
        registers.TryGetValue(this.registerToModify, out int modifyRegisterCurrentValue);

        if (this.CheckValueWithOperator(conditionRegisterCurrentValue))
        {
          registers[this.registerToModify] = this.GetNewValue(modifyRegisterCurrentValue);
          return registers[this.registerToModify];
        }

        return modifyRegisterCurrentValue;
      }

      private int GetNewValue(int oldValue)
      {
        if (this.modifier == Modifier.Inc)
        {
          return oldValue + this.modificationAmount;
        }
        else
        {
          return oldValue - this.modificationAmount;
        }
      }

      private bool CheckValueWithOperator(int value)
      {
        switch (this.conditionOperator)
        {
          case Operator.Greater:
            return value > this.conditionOperand;
          case Operator.Less:
            return value < this.conditionOperand;
          case Operator.GreaterOrEqual:
            return value >= this.conditionOperand;
          case Operator.LessOrEqual:
            return value <= this.conditionOperand;
          case Operator.NotEqual:
            return value != this.conditionOperand;
          case Operator.Equal:
            return value == this.conditionOperand;
        }

        Console.WriteLine("UNEXPECTED OPERATOR");
        return false;
      }
    }
  }
}

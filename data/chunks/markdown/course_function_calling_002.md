---
chunk_id: course_function_calling_002
source_url: https://tds.s-anand.net/#/function-calling
source_title: function-calling
content_type: course
tokens: 448
---

": {
 "type": "string",
 "description": "Name of the meeting room"
 }
 },
 "required": ["date", "time", "meeting_room"],
 "additionalProperties": False
 },
 "strict": True
 }
}
```

### How to define multiple functions

You can define multiple functions by passing a list of function definitions to the `tools` parameter.

---

Here's an example of a list of function definitions for handling employee expenses and calculating performance bonuses:

```python
tools = [
 {
 "type": "function",
 "function": {
 "name": "get_expense_balance",
 "description": "Get expense balance for an employee",
 "parameters": {
 "type": "object",
 "properties": {
 "employee_id": {
 "type": "integer",
 "description": "Employee ID number"
 }
 },
 "required": ["employee_id"],
 "additionalProperties": False
 },
 "strict": True
 }
 },
 {
 "type": "function",
 "function": {
 "name": "calculate_performance_bonus",
 "description": "Calculate yearly performance bonus for an employee",
 "parameters": {
 "type": "object",
 "properties": {
 "employee_id": {
 "type": "integer",
 "description": "Employee ID number"
 },
 "current_year": {
 "type": "integer",
 "description": "Year to calculate bonus for"
 }
 },
 "required": ["employee_id", "current_year"],
 "additionalProperties": False
 },
 "strict": True
 }
 }
]
```

Best Practices:

1. **Use Strict Mode**
 - Always set `strict: True` to ensure valid function calls
 - Define all required parameters
 - Set `additionalProperties: False`
2. **Use tool choice**
 - Set `tool_choice: "required"` to ensure that the model will always call one or more tools
 - The default is `tool_choice: "auto"` which means the model will choose a tool only if appropriate
3. **Clear Descriptions**
 - Write detailed function and parameter descriptions
 - Include expected formats and units
 - Mention any constraints or limitations
4. **Error Handling**
 - Validate function inputs before execution
 - Return clear error messages
 - Handle missing or invalid parameters

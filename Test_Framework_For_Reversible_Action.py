# Test_Framework_For_Reversible_Action
class Test_Framework_For_Reversible_Action:
    def __init__(self):
        self.tests = []

    def add_test(self, action_description, action, reverse_action, test_cases):
        """
        Add a test to the framework.
        
        Parameters:
        - action: the function to perform the action
        - reverse_action: the function to reverse the action
        - test_cases: a list of inputs to test the functions with
        """
        self.tests.append((action_description, action, reverse_action, test_cases))

    def run_tests(self):
        """
        Run all tests and print results.
        """
        for i, (action_description, action, reverse_action, test_cases) in enumerate(self.tests):
            print(f"Running Test {i + 1}: {action_description}")
            for test_case in test_cases:
                result = self.run_single_test(action, reverse_action, test_case)
                if result:
                    print(f"Test passed for input: {test_case}")
                else:
                    print(f"Test failed for input: {test_case}")
            
            print(f"===== Running Test {i + 1}: {action_description} [DONE] =====")

    def run_single_test(self, action, reverse_action, input_data):
        """
        Run a single test case.
        
        Parameters:
        - action: the function to perform the action
        - reverse_action: the function to reverse the action
        - input_data: the input data to test
        
        Returns:
        - True if the test passed, False otherwise
        """
        try:
            action_result = action(input_data)
            reverse_result = reverse_action(*action_result)
            return input_data == reverse_result
        except Exception as e:
            print(f"Error during test: {e}")
            return False


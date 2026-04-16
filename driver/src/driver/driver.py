"""
Example driver class for a machine.

All public methods should be documented with a docstring, arguments, and return type.

Methods that are not part of the puda CLI contract (helpers, one-off utilities, anything
the operator should not invoke as a machine command) must be private: define them with a
leading underscore (e.g. ``_poll_status``). Only public names are exposed to puda; private
names stay internal to this driver implementation.

The puda CLI maps public driver methods to ``puda machine <command> <machine_id>``. For
example: ``puda machine home <machine_id>`` and ``puda machine reset <machine_id>``.

They are optional but good to implement:
- ``home``
- ``reset``
"""

class Driver:
    def __init__(self):
        # connection logic here
        pass

    def home(self) -> bool:
        """
        Homes the machine
        
        Returns:
            bool: True if the home was successful, False otherwise
        """
        pass

    def reset(self) -> bool:
        """ 
        Software reset the machine
        
        Returns:
            bool: True if the reset was successful, False otherwise
        """
        pass
      
    def get_position(self):
        """
        Get the current position of the machine
        
        Returns:
            dict: A dictionary containing the current position of the machine
        """
        return {"x": 0, "y": 0, "z": 0}
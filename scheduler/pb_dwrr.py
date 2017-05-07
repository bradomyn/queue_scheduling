#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Cesar Prados (bradomyn@gmail.com)
#
# You should have received a copy of the GNU General Public License
# along with Hdlmake.  If not, see <http://www.gnu.org/licenses/>.

"""
Implements Priority-Based Deficit Weighted Round Robin
"""

class pb_dwrr:

    FLOWS = 8
    QUANTUM = (1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)
    WEIGTH = (20, 20, 20, 10, 10, 10, 5, 5)

    def __init__(self, flows = None, quantum = None, weigth = None):
        self.flows = flows if flows is not None else self.FLOWS
        self.quantum = quantum if quantum is not None else self.QUANTUM
        self.weigth = weigth if weigth is not None else self.WEIGTH
    

if __name__ == '__main__':
    scheduler = pb_dwrr()

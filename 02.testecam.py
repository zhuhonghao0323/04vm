# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import time

from source.models.eeam.model import EEAM

start = time.clock()
province = '山东'
model1 = EEAM(read_mid_data=True, recount=False, province=province)
model1.run()
end = time.clock()
runTime = end - start
print(runTime)

from source.models.ecam.model import ECAM
import time

start = time.clock()
province = '山东'
model1 = ECAM(read_mid_data=True, recount=False, province=province)
model1.run(gases_type='co2', )
end = time.clock()
runTime = end - start
print(runTime)

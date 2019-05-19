

cross-join N arrays

--[[tables in lua are like arrays
lua doesn't have a concatenate--]]


solution 1

local function concatArray(a, b)
  local result = {table.unpack(a)}
  table.move(b, 1, #b, #result + 1, result)
  return result
end

--[[tables in lua are like arrays
this method joins N arrays by merging tables--]]

solution 2

local function union ( x, y )
    local result = {}
    for u,v in pairs ( x ) do
        table.insert( result, v )
    end
    for u,v in pairs ( y ) do
         table.insert( result, v )
    end
    return result
end

--[[local fusedArray = {}
local n=0
for k,v in ipairs(array1) do n=n+1 ; fusedArray[n] = v end
for k,v in ipairs(array2) do n=n+1 ; fusedArray[n] = v end

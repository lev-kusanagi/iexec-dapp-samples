pragma solidity ^0.4.11;
import "iexec-oracle-contract/contracts/IexecOracleAPI.sol";
contract Tinychat2 is IexecOracleAPI{

    uint public constant DAPP_PRICE = 0;
    string public constant DAPP_NAME = "Tinychat2";
    
    function Tinychat2 (address _iexecOracleAddress) IexecOracleAPI(_iexecOracleAddress,DAPP_PRICE,DAPP_NAME){

    }

}

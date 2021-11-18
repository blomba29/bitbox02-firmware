"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import antiklepto_pb2
import builtins
import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BTCCoin(_BTCCoin, metaclass=_BTCCoinEnumTypeWrapper):
    pass
class _BTCCoin:
    V = typing.NewType('V', builtins.int)
class _BTCCoinEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BTCCoin.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    BTC = BTCCoin.V(0)
    TBTC = BTCCoin.V(1)
    LTC = BTCCoin.V(2)
    TLTC = BTCCoin.V(3)

BTC = BTCCoin.V(0)
TBTC = BTCCoin.V(1)
LTC = BTCCoin.V(2)
TLTC = BTCCoin.V(3)
global___BTCCoin = BTCCoin


class BTCOutputType(_BTCOutputType, metaclass=_BTCOutputTypeEnumTypeWrapper):
    pass
class _BTCOutputType:
    V = typing.NewType('V', builtins.int)
class _BTCOutputTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BTCOutputType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    UNKNOWN = BTCOutputType.V(0)
    P2PKH = BTCOutputType.V(1)
    P2SH = BTCOutputType.V(2)
    P2WPKH = BTCOutputType.V(3)
    P2WSH = BTCOutputType.V(4)

UNKNOWN = BTCOutputType.V(0)
P2PKH = BTCOutputType.V(1)
P2SH = BTCOutputType.V(2)
P2WPKH = BTCOutputType.V(3)
P2WSH = BTCOutputType.V(4)
global___BTCOutputType = BTCOutputType


class BTCScriptConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class SimpleType(_SimpleType, metaclass=_SimpleTypeEnumTypeWrapper):
        """SimpleType is a "simple" script: one public key, no additional inputs."""
        pass
    class _SimpleType:
        V = typing.NewType('V', builtins.int)
    class _SimpleTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SimpleType.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        P2WPKH_P2SH = BTCScriptConfig.SimpleType.V(0)
        P2WPKH = BTCScriptConfig.SimpleType.V(1)

    P2WPKH_P2SH = BTCScriptConfig.SimpleType.V(0)
    P2WPKH = BTCScriptConfig.SimpleType.V(1)

    class Multisig(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ScriptType(_ScriptType, metaclass=_ScriptTypeEnumTypeWrapper):
            pass
        class _ScriptType:
            V = typing.NewType('V', builtins.int)
        class _ScriptTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ScriptType.V], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
            P2WSH = BTCScriptConfig.Multisig.ScriptType.V(0)
            """native segwit v0 multisig (bech32 addresses)"""

            P2WSH_P2SH = BTCScriptConfig.Multisig.ScriptType.V(1)
            """wrapped segwit for legacy address compatibility"""


        P2WSH = BTCScriptConfig.Multisig.ScriptType.V(0)
        """native segwit v0 multisig (bech32 addresses)"""

        P2WSH_P2SH = BTCScriptConfig.Multisig.ScriptType.V(1)
        """wrapped segwit for legacy address compatibility"""


        THRESHOLD_FIELD_NUMBER: builtins.int
        XPUBS_FIELD_NUMBER: builtins.int
        OUR_XPUB_INDEX_FIELD_NUMBER: builtins.int
        SCRIPT_TYPE_FIELD_NUMBER: builtins.int
        threshold: builtins.int = ...
        @property
        def xpubs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common_pb2.XPub]:
            """xpubs are acount-level xpubs. Addresses are going to be derived from it using: m/<change>/<receive>.
            The number of xpubs defines the number of cosigners.
            """
            pass
        our_xpub_index: builtins.int = ...
        """Index to the xpub of our keystore in xpubs. The keypath to it is provided via
        BTCPubRequest/BTCSignInit.
        """

        script_type: global___BTCScriptConfig.Multisig.ScriptType.V = ...
        def __init__(self,
            *,
            threshold : builtins.int = ...,
            xpubs : typing.Optional[typing.Iterable[common_pb2.XPub]] = ...,
            our_xpub_index : builtins.int = ...,
            script_type : global___BTCScriptConfig.Multisig.ScriptType.V = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["our_xpub_index",b"our_xpub_index","script_type",b"script_type","threshold",b"threshold","xpubs",b"xpubs"]) -> None: ...

    SIMPLE_TYPE_FIELD_NUMBER: builtins.int
    MULTISIG_FIELD_NUMBER: builtins.int
    simple_type: global___BTCScriptConfig.SimpleType.V = ...
    @property
    def multisig(self) -> global___BTCScriptConfig.Multisig: ...
    def __init__(self,
        *,
        simple_type : global___BTCScriptConfig.SimpleType.V = ...,
        multisig : typing.Optional[global___BTCScriptConfig.Multisig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config","multisig",b"multisig","simple_type",b"simple_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","multisig",b"multisig","simple_type",b"simple_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config",b"config"]) -> typing.Optional[typing_extensions.Literal["simple_type","multisig"]]: ...
global___BTCScriptConfig = BTCScriptConfig

class BTCPubRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class XPubType(_XPubType, metaclass=_XPubTypeEnumTypeWrapper):
        pass
    class _XPubType:
        V = typing.NewType('V', builtins.int)
    class _XPubTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_XPubType.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TPUB = BTCPubRequest.XPubType.V(0)
        XPUB = BTCPubRequest.XPubType.V(1)
        YPUB = BTCPubRequest.XPubType.V(2)
        ZPUB = BTCPubRequest.XPubType.V(3)
        """zpub"""

        VPUB = BTCPubRequest.XPubType.V(4)
        """vpub"""

        UPUB = BTCPubRequest.XPubType.V(5)
        CAPITAL_VPUB = BTCPubRequest.XPubType.V(6)
        """Vpub"""

        CAPITAL_ZPUB = BTCPubRequest.XPubType.V(7)
        """Zpub"""

        CAPITAL_UPUB = BTCPubRequest.XPubType.V(8)
        """Upub"""

        CAPITAL_YPUB = BTCPubRequest.XPubType.V(9)
        """Ypub"""


    TPUB = BTCPubRequest.XPubType.V(0)
    XPUB = BTCPubRequest.XPubType.V(1)
    YPUB = BTCPubRequest.XPubType.V(2)
    ZPUB = BTCPubRequest.XPubType.V(3)
    """zpub"""

    VPUB = BTCPubRequest.XPubType.V(4)
    """vpub"""

    UPUB = BTCPubRequest.XPubType.V(5)
    CAPITAL_VPUB = BTCPubRequest.XPubType.V(6)
    """Vpub"""

    CAPITAL_ZPUB = BTCPubRequest.XPubType.V(7)
    """Zpub"""

    CAPITAL_UPUB = BTCPubRequest.XPubType.V(8)
    """Upub"""

    CAPITAL_YPUB = BTCPubRequest.XPubType.V(9)
    """Ypub"""


    COIN_FIELD_NUMBER: builtins.int
    KEYPATH_FIELD_NUMBER: builtins.int
    XPUB_TYPE_FIELD_NUMBER: builtins.int
    SCRIPT_CONFIG_FIELD_NUMBER: builtins.int
    DISPLAY_FIELD_NUMBER: builtins.int
    coin: global___BTCCoin.V = ...
    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    xpub_type: global___BTCPubRequest.XPubType.V = ...
    @property
    def script_config(self) -> global___BTCScriptConfig: ...
    display: builtins.bool = ...
    def __init__(self,
        *,
        coin : global___BTCCoin.V = ...,
        keypath : typing.Optional[typing.Iterable[builtins.int]] = ...,
        xpub_type : global___BTCPubRequest.XPubType.V = ...,
        script_config : typing.Optional[global___BTCScriptConfig] = ...,
        display : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["output",b"output","script_config",b"script_config","xpub_type",b"xpub_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["coin",b"coin","display",b"display","keypath",b"keypath","output",b"output","script_config",b"script_config","xpub_type",b"xpub_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["output",b"output"]) -> typing.Optional[typing_extensions.Literal["xpub_type","script_config"]]: ...
global___BTCPubRequest = BTCPubRequest

class BTCScriptConfigWithKeypath(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SCRIPT_CONFIG_FIELD_NUMBER: builtins.int
    KEYPATH_FIELD_NUMBER: builtins.int
    @property
    def script_config(self) -> global___BTCScriptConfig: ...
    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        script_config : typing.Optional[global___BTCScriptConfig] = ...,
        keypath : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["script_config",b"script_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["keypath",b"keypath","script_config",b"script_config"]) -> None: ...
global___BTCScriptConfigWithKeypath = BTCScriptConfigWithKeypath

class BTCSignInitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COIN_FIELD_NUMBER: builtins.int
    SCRIPT_CONFIGS_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    NUM_INPUTS_FIELD_NUMBER: builtins.int
    NUM_OUTPUTS_FIELD_NUMBER: builtins.int
    LOCKTIME_FIELD_NUMBER: builtins.int
    coin: global___BTCCoin.V = ...
    @property
    def script_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BTCScriptConfigWithKeypath]:
        """used script configs in inputs and changes"""
        pass
    version: builtins.int = ...
    """must be 1 or 2"""

    num_inputs: builtins.int = ...
    num_outputs: builtins.int = ...
    locktime: builtins.int = ...
    """must be <500000000"""

    def __init__(self,
        *,
        coin : global___BTCCoin.V = ...,
        script_configs : typing.Optional[typing.Iterable[global___BTCScriptConfigWithKeypath]] = ...,
        version : builtins.int = ...,
        num_inputs : builtins.int = ...,
        num_outputs : builtins.int = ...,
        locktime : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["coin",b"coin","locktime",b"locktime","num_inputs",b"num_inputs","num_outputs",b"num_outputs","script_configs",b"script_configs","version",b"version"]) -> None: ...
global___BTCSignInitRequest = BTCSignInitRequest

class BTCSignNextResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        pass
    class _Type:
        V = typing.NewType('V', builtins.int)
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INPUT = BTCSignNextResponse.Type.V(0)
        OUTPUT = BTCSignNextResponse.Type.V(1)
        DONE = BTCSignNextResponse.Type.V(2)
        PREVTX_INIT = BTCSignNextResponse.Type.V(3)
        """For the previous transaction at input `index`."""

        PREVTX_INPUT = BTCSignNextResponse.Type.V(4)
        PREVTX_OUTPUT = BTCSignNextResponse.Type.V(5)
        HOST_NONCE = BTCSignNextResponse.Type.V(6)

    INPUT = BTCSignNextResponse.Type.V(0)
    OUTPUT = BTCSignNextResponse.Type.V(1)
    DONE = BTCSignNextResponse.Type.V(2)
    PREVTX_INIT = BTCSignNextResponse.Type.V(3)
    """For the previous transaction at input `index`."""

    PREVTX_INPUT = BTCSignNextResponse.Type.V(4)
    PREVTX_OUTPUT = BTCSignNextResponse.Type.V(5)
    HOST_NONCE = BTCSignNextResponse.Type.V(6)

    TYPE_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    HAS_SIGNATURE_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    PREV_INDEX_FIELD_NUMBER: builtins.int
    ANTI_KLEPTO_SIGNER_COMMITMENT_FIELD_NUMBER: builtins.int
    type: global___BTCSignNextResponse.Type.V = ...
    index: builtins.int = ...
    """index of the current input or output"""

    has_signature: builtins.bool = ...
    """only as a response to BTCSignInputRequest"""

    signature: builtins.bytes = ...
    """64 bytes (32 bytes big endian R, 32 bytes big endian S). Only if has_signature is true."""

    prev_index: builtins.int = ...
    """Previous tx's input/output index in case of PREV_INPUT or PREV_OUTPUT, for the input at `index`."""

    @property
    def anti_klepto_signer_commitment(self) -> antiklepto_pb2.AntiKleptoSignerCommitment: ...
    def __init__(self,
        *,
        type : global___BTCSignNextResponse.Type.V = ...,
        index : builtins.int = ...,
        has_signature : builtins.bool = ...,
        signature : builtins.bytes = ...,
        prev_index : builtins.int = ...,
        anti_klepto_signer_commitment : typing.Optional[antiklepto_pb2.AntiKleptoSignerCommitment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["anti_klepto_signer_commitment",b"anti_klepto_signer_commitment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["anti_klepto_signer_commitment",b"anti_klepto_signer_commitment","has_signature",b"has_signature","index",b"index","prev_index",b"prev_index","signature",b"signature","type",b"type"]) -> None: ...
global___BTCSignNextResponse = BTCSignNextResponse

class BTCSignInputRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PREVOUTHASH_FIELD_NUMBER: builtins.int
    PREVOUTINDEX_FIELD_NUMBER: builtins.int
    PREVOUTVALUE_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    KEYPATH_FIELD_NUMBER: builtins.int
    SCRIPT_CONFIG_INDEX_FIELD_NUMBER: builtins.int
    HOST_NONCE_COMMITMENT_FIELD_NUMBER: builtins.int
    prevOutHash: builtins.bytes = ...
    prevOutIndex: builtins.int = ...
    prevOutValue: builtins.int = ...
    sequence: builtins.int = ...
    """must be 0xffffffff-2, 0xffffffff-1 or 0xffffffff"""

    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """all inputs must be ours."""
        pass
    script_config_index: builtins.int = ...
    """References a script config from BTCSignInitRequest"""

    @property
    def host_nonce_commitment(self) -> antiklepto_pb2.AntiKleptoHostNonceCommitment: ...
    def __init__(self,
        *,
        prevOutHash : builtins.bytes = ...,
        prevOutIndex : builtins.int = ...,
        prevOutValue : builtins.int = ...,
        sequence : builtins.int = ...,
        keypath : typing.Optional[typing.Iterable[builtins.int]] = ...,
        script_config_index : builtins.int = ...,
        host_nonce_commitment : typing.Optional[antiklepto_pb2.AntiKleptoHostNonceCommitment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["host_nonce_commitment",b"host_nonce_commitment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["host_nonce_commitment",b"host_nonce_commitment","keypath",b"keypath","prevOutHash",b"prevOutHash","prevOutIndex",b"prevOutIndex","prevOutValue",b"prevOutValue","script_config_index",b"script_config_index","sequence",b"sequence"]) -> None: ...
global___BTCSignInputRequest = BTCSignInputRequest

class BTCSignOutputRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OURS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    KEYPATH_FIELD_NUMBER: builtins.int
    SCRIPT_CONFIG_INDEX_FIELD_NUMBER: builtins.int
    ours: builtins.bool = ...
    type: global___BTCOutputType.V = ...
    """if ours is false"""

    value: builtins.int = ...
    """20 bytes for p2pkh, p2sh, pw2wpkh. 32 bytes for p2wsh."""

    hash: builtins.bytes = ...
    """if ours is false"""

    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """if ours is true"""
        pass
    script_config_index: builtins.int = ...
    """If ours is true. References a script config from BTCSignInitRequest"""

    def __init__(self,
        *,
        ours : builtins.bool = ...,
        type : global___BTCOutputType.V = ...,
        value : builtins.int = ...,
        hash : builtins.bytes = ...,
        keypath : typing.Optional[typing.Iterable[builtins.int]] = ...,
        script_config_index : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash",b"hash","keypath",b"keypath","ours",b"ours","script_config_index",b"script_config_index","type",b"type","value",b"value"]) -> None: ...
global___BTCSignOutputRequest = BTCSignOutputRequest

class BTCScriptConfigRegistration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COIN_FIELD_NUMBER: builtins.int
    SCRIPT_CONFIG_FIELD_NUMBER: builtins.int
    KEYPATH_FIELD_NUMBER: builtins.int
    coin: global___BTCCoin.V = ...
    @property
    def script_config(self) -> global___BTCScriptConfig: ...
    @property
    def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        coin : global___BTCCoin.V = ...,
        script_config : typing.Optional[global___BTCScriptConfig] = ...,
        keypath : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["script_config",b"script_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["coin",b"coin","keypath",b"keypath","script_config",b"script_config"]) -> None: ...
global___BTCScriptConfigRegistration = BTCScriptConfigRegistration

class BTCSuccess(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___BTCSuccess = BTCSuccess

class BTCIsScriptConfigRegisteredRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REGISTRATION_FIELD_NUMBER: builtins.int
    @property
    def registration(self) -> global___BTCScriptConfigRegistration: ...
    def __init__(self,
        *,
        registration : typing.Optional[global___BTCScriptConfigRegistration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["registration",b"registration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["registration",b"registration"]) -> None: ...
global___BTCIsScriptConfigRegisteredRequest = BTCIsScriptConfigRegisteredRequest

class BTCIsScriptConfigRegisteredResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IS_REGISTERED_FIELD_NUMBER: builtins.int
    is_registered: builtins.bool = ...
    def __init__(self,
        *,
        is_registered : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_registered",b"is_registered"]) -> None: ...
global___BTCIsScriptConfigRegisteredResponse = BTCIsScriptConfigRegisteredResponse

class BTCRegisterScriptConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class XPubType(_XPubType, metaclass=_XPubTypeEnumTypeWrapper):
        pass
    class _XPubType:
        V = typing.NewType('V', builtins.int)
    class _XPubTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_XPubType.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        AUTO_ELECTRUM = BTCRegisterScriptConfigRequest.XPubType.V(0)
        """Automatically choose to match Electrum's xpub format (e.g. Zpub/Vpub for p2wsh multisig mainnet/testnet)."""

        AUTO_XPUB_TPUB = BTCRegisterScriptConfigRequest.XPubType.V(1)
        """Always xpub for mainnets, tpub for testnets."""


    AUTO_ELECTRUM = BTCRegisterScriptConfigRequest.XPubType.V(0)
    """Automatically choose to match Electrum's xpub format (e.g. Zpub/Vpub for p2wsh multisig mainnet/testnet)."""

    AUTO_XPUB_TPUB = BTCRegisterScriptConfigRequest.XPubType.V(1)
    """Always xpub for mainnets, tpub for testnets."""


    REGISTRATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    XPUB_TYPE_FIELD_NUMBER: builtins.int
    @property
    def registration(self) -> global___BTCScriptConfigRegistration: ...
    name: typing.Text = ...
    """If empty, the name is entered on the device instead."""

    xpub_type: global___BTCRegisterScriptConfigRequest.XPubType.V = ...
    def __init__(self,
        *,
        registration : typing.Optional[global___BTCScriptConfigRegistration] = ...,
        name : typing.Text = ...,
        xpub_type : global___BTCRegisterScriptConfigRequest.XPubType.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["registration",b"registration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","registration",b"registration","xpub_type",b"xpub_type"]) -> None: ...
global___BTCRegisterScriptConfigRequest = BTCRegisterScriptConfigRequest

class BTCPrevTxInitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSION_FIELD_NUMBER: builtins.int
    NUM_INPUTS_FIELD_NUMBER: builtins.int
    NUM_OUTPUTS_FIELD_NUMBER: builtins.int
    LOCKTIME_FIELD_NUMBER: builtins.int
    version: builtins.int = ...
    num_inputs: builtins.int = ...
    num_outputs: builtins.int = ...
    locktime: builtins.int = ...
    def __init__(self,
        *,
        version : builtins.int = ...,
        num_inputs : builtins.int = ...,
        num_outputs : builtins.int = ...,
        locktime : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["locktime",b"locktime","num_inputs",b"num_inputs","num_outputs",b"num_outputs","version",b"version"]) -> None: ...
global___BTCPrevTxInitRequest = BTCPrevTxInitRequest

class BTCPrevTxInputRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PREV_OUT_HASH_FIELD_NUMBER: builtins.int
    PREV_OUT_INDEX_FIELD_NUMBER: builtins.int
    SIGNATURE_SCRIPT_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    prev_out_hash: builtins.bytes = ...
    prev_out_index: builtins.int = ...
    signature_script: builtins.bytes = ...
    sequence: builtins.int = ...
    def __init__(self,
        *,
        prev_out_hash : builtins.bytes = ...,
        prev_out_index : builtins.int = ...,
        signature_script : builtins.bytes = ...,
        sequence : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["prev_out_hash",b"prev_out_hash","prev_out_index",b"prev_out_index","sequence",b"sequence","signature_script",b"signature_script"]) -> None: ...
global___BTCPrevTxInputRequest = BTCPrevTxInputRequest

class BTCPrevTxOutputRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUE_FIELD_NUMBER: builtins.int
    PUBKEY_SCRIPT_FIELD_NUMBER: builtins.int
    value: builtins.int = ...
    pubkey_script: builtins.bytes = ...
    def __init__(self,
        *,
        value : builtins.int = ...,
        pubkey_script : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pubkey_script",b"pubkey_script","value",b"value"]) -> None: ...
global___BTCPrevTxOutputRequest = BTCPrevTxOutputRequest

class BTCSignMessageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COIN_FIELD_NUMBER: builtins.int
    SCRIPT_CONFIG_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    HOST_NONCE_COMMITMENT_FIELD_NUMBER: builtins.int
    coin: global___BTCCoin.V = ...
    @property
    def script_config(self) -> global___BTCScriptConfigWithKeypath: ...
    msg: builtins.bytes = ...
    @property
    def host_nonce_commitment(self) -> antiklepto_pb2.AntiKleptoHostNonceCommitment: ...
    def __init__(self,
        *,
        coin : global___BTCCoin.V = ...,
        script_config : typing.Optional[global___BTCScriptConfigWithKeypath] = ...,
        msg : builtins.bytes = ...,
        host_nonce_commitment : typing.Optional[antiklepto_pb2.AntiKleptoHostNonceCommitment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["host_nonce_commitment",b"host_nonce_commitment","script_config",b"script_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["coin",b"coin","host_nonce_commitment",b"host_nonce_commitment","msg",b"msg","script_config",b"script_config"]) -> None: ...
global___BTCSignMessageRequest = BTCSignMessageRequest

class BTCSignMessageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SIGNATURE_FIELD_NUMBER: builtins.int
    signature: builtins.bytes = ...
    """65 bytes (32 bytes big endian R, 32 bytes big endian S, 1 recid)."""

    def __init__(self,
        *,
        signature : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["signature",b"signature"]) -> None: ...
global___BTCSignMessageResponse = BTCSignMessageResponse

class BTCRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IS_SCRIPT_CONFIG_REGISTERED_FIELD_NUMBER: builtins.int
    REGISTER_SCRIPT_CONFIG_FIELD_NUMBER: builtins.int
    PREVTX_INIT_FIELD_NUMBER: builtins.int
    PREVTX_INPUT_FIELD_NUMBER: builtins.int
    PREVTX_OUTPUT_FIELD_NUMBER: builtins.int
    SIGN_MESSAGE_FIELD_NUMBER: builtins.int
    ANTIKLEPTO_SIGNATURE_FIELD_NUMBER: builtins.int
    @property
    def is_script_config_registered(self) -> global___BTCIsScriptConfigRegisteredRequest: ...
    @property
    def register_script_config(self) -> global___BTCRegisterScriptConfigRequest: ...
    @property
    def prevtx_init(self) -> global___BTCPrevTxInitRequest: ...
    @property
    def prevtx_input(self) -> global___BTCPrevTxInputRequest: ...
    @property
    def prevtx_output(self) -> global___BTCPrevTxOutputRequest: ...
    @property
    def sign_message(self) -> global___BTCSignMessageRequest: ...
    @property
    def antiklepto_signature(self) -> antiklepto_pb2.AntiKleptoSignatureRequest: ...
    def __init__(self,
        *,
        is_script_config_registered : typing.Optional[global___BTCIsScriptConfigRegisteredRequest] = ...,
        register_script_config : typing.Optional[global___BTCRegisterScriptConfigRequest] = ...,
        prevtx_init : typing.Optional[global___BTCPrevTxInitRequest] = ...,
        prevtx_input : typing.Optional[global___BTCPrevTxInputRequest] = ...,
        prevtx_output : typing.Optional[global___BTCPrevTxOutputRequest] = ...,
        sign_message : typing.Optional[global___BTCSignMessageRequest] = ...,
        antiklepto_signature : typing.Optional[antiklepto_pb2.AntiKleptoSignatureRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["antiklepto_signature",b"antiklepto_signature","is_script_config_registered",b"is_script_config_registered","prevtx_init",b"prevtx_init","prevtx_input",b"prevtx_input","prevtx_output",b"prevtx_output","register_script_config",b"register_script_config","request",b"request","sign_message",b"sign_message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["antiklepto_signature",b"antiklepto_signature","is_script_config_registered",b"is_script_config_registered","prevtx_init",b"prevtx_init","prevtx_input",b"prevtx_input","prevtx_output",b"prevtx_output","register_script_config",b"register_script_config","request",b"request","sign_message",b"sign_message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["request",b"request"]) -> typing.Optional[typing_extensions.Literal["is_script_config_registered","register_script_config","prevtx_init","prevtx_input","prevtx_output","sign_message","antiklepto_signature"]]: ...
global___BTCRequest = BTCRequest

class BTCResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUCCESS_FIELD_NUMBER: builtins.int
    IS_SCRIPT_CONFIG_REGISTERED_FIELD_NUMBER: builtins.int
    SIGN_NEXT_FIELD_NUMBER: builtins.int
    SIGN_MESSAGE_FIELD_NUMBER: builtins.int
    ANTIKLEPTO_SIGNER_COMMITMENT_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> global___BTCSuccess: ...
    @property
    def is_script_config_registered(self) -> global___BTCIsScriptConfigRegisteredResponse: ...
    @property
    def sign_next(self) -> global___BTCSignNextResponse: ...
    @property
    def sign_message(self) -> global___BTCSignMessageResponse: ...
    @property
    def antiklepto_signer_commitment(self) -> antiklepto_pb2.AntiKleptoSignerCommitment: ...
    def __init__(self,
        *,
        success : typing.Optional[global___BTCSuccess] = ...,
        is_script_config_registered : typing.Optional[global___BTCIsScriptConfigRegisteredResponse] = ...,
        sign_next : typing.Optional[global___BTCSignNextResponse] = ...,
        sign_message : typing.Optional[global___BTCSignMessageResponse] = ...,
        antiklepto_signer_commitment : typing.Optional[antiklepto_pb2.AntiKleptoSignerCommitment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["antiklepto_signer_commitment",b"antiklepto_signer_commitment","is_script_config_registered",b"is_script_config_registered","response",b"response","sign_message",b"sign_message","sign_next",b"sign_next","success",b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["antiklepto_signer_commitment",b"antiklepto_signer_commitment","is_script_config_registered",b"is_script_config_registered","response",b"response","sign_message",b"sign_message","sign_next",b"sign_next","success",b"success"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["response",b"response"]) -> typing.Optional[typing_extensions.Literal["success","is_script_config_registered","sign_next","sign_message","antiklepto_signer_commitment"]]: ...
global___BTCResponse = BTCResponse

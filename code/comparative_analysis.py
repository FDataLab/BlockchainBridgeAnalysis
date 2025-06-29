import pandas as pd

df = pd.read_csv("merged_full_summary.csv")
df["Address"] = df["Address"].str.lower()

# Known exploit addresses
exploit_data = {
    "0xc8a65fadf0e0ddaf421f28feab69bf6e2e589963": {
        "name": "Poly Network Trusted State Root Exploit1",
        "attack_date": "2021-08-10"
    },
    "0x5dc3603c9d42ff184153a8a9094a73d461663214": {
        "name": "Poly Network Trusted State Root Exploit2",
        "attack_date": "2021-08-10"
    },
    "0x1234567890abcdef1234567890abcdef12345678": {
        "name": "Multichain Rush Attack",
        "attack_date": "2023-02-15"
    },
    "0x489a8756c18c0b8b24ec2a2b9ff3d4d447f79bec": {
        "name": "Binance Bridge Proof Verifier Bug",
        "attack_date": "2022-10-06"
    },
    "0x82faed2da812d2e5cced3c12b3baeb1a522dc677": {
        "name": "Omni Bridge ChainID vulnerability exploit",
        "attack_date": "2022-09-18"
    },
    "0xb5c55f76f90cc528b2609109ca14d8d84593590e": {
        "name": "Nomad Trusted State Root Exploit",
        "attack_date": "2022-08-01"
    },
    "0x0d043128146654c7683fbf30ac98d7b2285ded00": {
        "name": "Horizon Bridge Private Key Compromised",
        "attack_date": "2022-06-24"
    },
    "0x098b716b8aaf21512996dc57eb0615e2383e2f96": {
        "name": "Ronin Private Key Compromised (Social Engineering)",
        "attack_date": "2022-03-23"
    },
    "0x629e7da20197a5429d30da36e77d06cdf796b71a": {
        "name": "Wormhole Account Spoofing",
        "attack_date": "2022-02-02"
    },
    "0xd01ae1a708614948b2b5e0b7ab5be6afa01325c7": {
        "name": "Qubit Finance Deposit Function Exploit",
        "attack_date": "2022-01-28"
    },
    "0x8c1944FAC705ef172f21f905b5523Ae260F76d62": {
        "name": "Thorchain Private Key Compromised (Phishing Attack)",
        "attack_date": "2021-07-24"
    },
    "0x00fac92881556a90fdb19eae9f23640b95b4bcbd": {
        "name": "KiloEx Oracle Manipulation Attack",
        "attack_date": "2025-04-14"
    },
    "0x551f3110f12c763D1611d5A63B5F015d1c1a954C": {
        "name": "KiloEx Oracle Manipulation Attack",
        "attack_date": "2025-04-14"
    },
    "0x27055aE433E9DCb30f6EbCC1A374Cf5CC03C484E": {
        "name": "ALEX Bridge Hack",
        "attack_date": "2024-05-14"
    },
    "0x9d5765ae1c95c21d4cc3b1d5bba71bad3b012b68":{
        "name": "Multichain Bridge Hack1",
        "attack_date": "2023-07-07"
    },
    "0xefeef8e968a0db92781ac7b3b7c821909ef10c88":{
        "name": "Multichain Bridge Hack2",
        "attack_date": "2023-07-07"
    },
    "0x418ed2554c010a0c63024d1da3a93b4dc26e5bb7":{
        "name": "Multichain Bridge Hack3",
        "attack_date": "2023-07-07"
    },
    "0x622e5f32e9ed5318d3a05ee2932fd3e118347ba0":{
        "name": "Multichain Bridge Hack4",
        "attack_date": "2023-07-07"
    },
    "0x48bead89e696ee93b04913cb0006f35adb844537":{
        "name": "Multichain Bridge Hack5",
        "attack_date": "2023-07-07"
    },
    "0x027f1571aca57354223276722dc7b572a5b05cd8":{
        "name": "Multichain Bridge Hack6",
        "attack_date": "2023-07-07"
    },
    "0x56D8B635A7C88Fd1104D23d632AF40c1C3Aac4e3": {
        "name": "Nomad Trusted State Root Exploit2",
        "attack_date": "2022-08-01"
    },
    "0xBF293D5138a2a1BA407B43672643434C43827179": {
        "name": "Nomad Trusted State Root Exploit3",
        "attack_date": "2022-08-01"
    },
    "0xe0Afadad1d93704761c8550F21A53DE3468Ba599": {
        "name": "Poly Network Hack",
        "attack_date": "2023-07-02"
    }
}

# Feature columns to compare
feature_cols = [
    "#TXBeforeAttack", "#TXAfterAttack", "#TXOnAttackDay",
    "#IntTXBeforeAttack", "#IntTXAfterAttack", "#IntTXOnAttackDay"
]

results = []

# Analyze each exploit address
for addr, name in exploit_data.items():
    addr = addr.lower()
    row = df[df["Address"] == addr]

    if row.empty:
        results.append({
            "Address": addr,
            "ExploitName": name,
            "MatchCount": 0,
            "#TXBeforeAttack": 0,
            "#TXAfterAttack": 0,
            "#TXOnAttackDay": 0,
            "#IntTXBeforeAttack": 0,
            "#IntTXAfterAttack": 0,
            "#IntTXOnAttackDay": 0,
        })
        continue

    features = row[feature_cols].iloc[0]
    matches = (df[feature_cols] == features).all(axis=1)
    match_count = matches.sum() - 1

    results.append({
        "Address": addr,
        "ExploitName": name,
        "MatchCount": match_count,
        **features.to_dict()  # unpack the feature values into the row
    })

result_df = pd.DataFrame(results)
print(result_df)

result_df.to_csv("exploit_feature_match_counts.csv", index=False)

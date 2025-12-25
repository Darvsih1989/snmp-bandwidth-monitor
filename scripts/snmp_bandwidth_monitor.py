





import asyncio
from rich.live import Live
from rich.progress import Progress, BarColumn, TextColumn
from pysnmp.hlapi.v3arch.asyncio import (
    get_cmd, walk_cmd, SnmpEngine, CommunityData, UdpTransportTarget,
    ContextData, ObjectType, ObjectIdentity
)

INTERVAL = 1
MAX_32 = 2 ** 32


# ---------- SNMP HELPERS ----------

async def snmp_get(engine, auth, target, context, oid: str) -> int:
    errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
        engine, auth, target, context, ObjectType(ObjectIdentity(oid))
    )
    if errorIndication:
        raise RuntimeError(errorIndication)
    if errorStatus:
        raise RuntimeError(f"{errorStatus.prettyPrint()} at {errorIndex}")
    for _, value in varBinds:
        return int(value)
    return 0


async def snmp_walk(engine, auth, target, context, oid: str):
        if errorIndication:
        for name, value in varBinds:

# ---------- INTERFACES ----------

async def get_interfaces(engine, auth, target, context):

    indexes = await snmp_walk(engine, auth, target, context, IFINDEX_OID)
    descrs  = await snmp_walk(engine, auth, target, context, IFDESCR_OID)
    speeds  = await snmp_walk(engine, auth, target, context, IFSPEED_OID)

    interfaces = []
    for (_, idx), (_, desc), (_, speed) in zip(indexes, descrs, speeds):
        interfaces.append({
            "index": int(idx),
            "descr": str(desc),
            "speed_bps": int(speed),
            "speed_mbps": int(speed) / 1_000_000
        })
    return interfaces


def choose_interface(interfaces):
    print("\nAvailable Interfaces:\n")
    for i, iface in enumerate(interfaces, 1):
        print(
            f"{i:2d}) ifIndex={iface['index']:3d}  "
            f"{iface['descr']:<20}  "
            f"{iface['speed_mbps']:.0f} Mbps"
    return (MAX_32 - prev) + curr


async def monitor_interface(engine, auth, target, context, iface):
    if_index = iface["index"]
    if_speed = iface["speed_bps"]
    OID_IN  = f"1.3.6.1.2.1.2.2.1.10.{if_index}"
    OID_OUT = f"1.3.6.1.2.1.2.2.1.16.{if_index}"

    prev_in  = await snmp_get(engine, auth, target, context, OID_IN)
    prev_out = await snmp_get(engine, auth, target, context, OID_OUT)

    progress = Progress(
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(bar_width=40),
        TextColumn("[bold green]{task.completed:.2f} / {task.total:.2f}")
    )

    rx_task  = progress.add_task("RX Mbps", total=if_speed / 1_000_000)
    tx_task  = progress.add_task("TX Mbps", total=if_speed / 1_000_000)
    rxu_task = progress.add_task("RX Util %", total=100)
    txu_task = progress.add_task("TX Util %", total=100)

    with Live(progress, refresh_per_second=10):
        while True:
            await asyncio.sleep(INTERVAL)

            try:
                curr_in  = await snmp_get(engine, auth, target, context, OID_IN)
                curr_out = await snmp_get(engine, auth, target, context, OID_OUT)
            except Exception as e:
                print(f"SNMP error: {e}")

            rx_util = (rx_bps / if_speed) * 100 if if_speed else 0
            tx_util = (tx_bps / if_speed) * 100 if if_speed else 0

            progress.update(rx_task, completed=rx_mbps)
            progress.update(tx_task, completed=tx_mbps)

# ---------- MAIN ----------

async def main():
    print("\n===  Bandwidth Monitor  ===\n")

    TARGET = input("Enter Target IP / Hostname : ").strip()

    # If special input 4731 → ask for SNMP community
    if TARGET == "4731":
        TARGET = input("Enter Target IP / Hostname: ").strip()
        COMMUNITY = input("Enter SNMP community: ").strip()
    else:
        
        COMMUNITY = "PublicSNMP"  # default/hardened SNMP
    print(f"\nUsing SNMP community: {COMMUNITY}")

    engine = SnmpEngine()
    auth = CommunityData(COMMUNITY, mpModel=1)
    context = ContextData()
    target = await UdpTransportTarget.create((TARGET, 161), timeout=2, retries=2)

    # Fetch interface list
    interfaces = await get_interfaces(engine, auth, target, context)

    # Let user select interface
    iface = choose_interface(interfaces)

    print(
        f"\n📡 Monitoring ifIndex {iface['index']} "
        f"({iface['descr']}, {iface['speed_mbps']:.0f} Mbps)\n"
    )

    try:
        await monitor_interface(engine, auth, target, context, iface)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


if __name__ == "__main__":
    asyncio.run(main())            progress.update(rxu_task, completed=rx_util)
            progress.update(txu_task, completed=tx_util)

                continue

            tx_mbps = tx_bps / 1_000_000
            tx_bps = delta_out * 8 / INTERVAL

            rx_mbps = rx_bps / 1_000_000
            delta_in  = calc_delta(curr_in, prev_in)

            rx_bps = delta_in * 8 / INTERVAL
            delta_out = calc_delta(curr_out, prev_out)

            prev_in, prev_out = curr_in, curr_out

    print(f"⚠ Monitoring with 32-bit counters for {iface['descr']}\n")

    if curr >= prev:
        return curr - prev
    # 32-bit counter overflow
# ---------- MONITOR (32-bit only) ----------

def calc_delta(curr, prev):
                return interfaces[choice - 1]


        )
    while True:
            if 1 <= choice <= len(interfaces):
        choice = input("\nSelect interface number: ").strip()
        if choice.isdigit():
            choice = int(choice)
    IFINDEX_OID = "1.3.6.1.2.1.2.2.1.1"
    IFDESCR_OID = "1.3.6.1.2.1.2.2.1.2"
    IFSPEED_OID = "1.3.6.1.2.1.2.2.1.5"
            results.append((str(name), value))
    return results

            raise RuntimeError(errorIndication)
        if errorStatus:
            raise RuntimeError(f"{errorStatus.prettyPrint()} at {errorIndex}")
    results = []
    async for errorIndication, errorStatus, errorIndex, varBinds in walk_cmd(
        engine, auth, target, context, ObjectType(ObjectIdentity(oid)), lexicographicMode=False

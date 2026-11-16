import React from 'react';
import {
	AbsoluteFill, Composition, Img, interpolate, spring, staticFile,
	useCurrentFrame, useVideoConfig, Easing,
} from 'remotion';

// ---------- tema ----------
const C = {
	bg: '#0d1524', bg2: '#16233a', red: '#c8102e', blue: '#2f9df4', redSoft: '#f04a5f', white: '#f5f7fb',
	muted: '#9fb0c8', card: '#ffffff', ink: '#111827', gold: '#f2b705', wire: '#cfd8e6',
};
const FONT = 'Inter, "DejaVu Sans", sans-serif';

type Cues = Record<string, number>;
type Props = {visual: any; dur: number; cues: Cues; panel?: boolean; brand?: string};
const BrandCtx = React.createContext('Experiencia 4 · Circuitos resistivos y ley de Ohm');
const PanelCtx = React.createContext(false);

const useT = () => {
	const f = useCurrentFrame();
	const {fps} = useVideoConfig();
	return f / fps;
};
// aparición suave a partir del segundo `at`
const useIn = (at: number, len = 0.5) => {
	const f = useCurrentFrame();
	const {fps} = useVideoConfig();
	return spring({frame: f - Math.round(at * fps), fps, config: {damping: 200}, durationInFrames: Math.round(len * fps)});
};
const cueAt = (cues: Cues, c?: string, fallback = 0.3) => (c && cues[c] !== undefined ? cues[c] : fallback);

// ---------- marco común ----------
const Frame: React.FC<{heading?: string; bg?: string; children: React.ReactNode; dur: number}> = ({heading, bg, children, dur}) => {
	const t = useT();
	const head = useIn(0.05, 0.6);
	const fadeOut = interpolate(t, [dur - 0.35, dur], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	const panel = React.useContext(PanelCtx);
	return (
		<AbsoluteFill style={{background: panel ? 'transparent' : `radial-gradient(ellipse at 20% 0%, ${C.bg2} 0%, ${C.bg} 65%)`, fontFamily: FONT, color: C.white}}>
			{panel ? <Box /> : null}
			<AbsoluteFill style={{opacity: fadeOut}}>
			{bg && !panel ? (
				<AbsoluteFill>
					<Img src={staticFile(bg)} style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(22px) brightness(0.35)', transform: 'scale(1.1)'}} />
				</AbsoluteFill>
			) : null}
			<div style={{position: 'absolute', left: 96, top: 54, fontSize: 22, letterSpacing: 3, color: C.muted, textTransform: 'uppercase'}}>
				{React.useContext(BrandCtx)}
			</div>
			{heading ? (
				<div style={{position: 'absolute', left: 96, top: 100, display: 'flex', alignItems: 'center', gap: 22,
					opacity: head, transform: `translateX(${(1 - head) * -40}px)`}}>
					<div style={{width: 10, height: 64, background: C.red, borderRadius: 4}} />
					<div style={{fontSize: 56, fontWeight: 700, letterSpacing: -0.5}}>{heading}</div>
				</div>
			) : null}
			<div style={{position: 'absolute', left: 96, right: 96, top: 210, bottom: panel ? 70 : 150}}>{children}</div>
			</AbsoluteFill>
		</AbsoluteFill>
	);
};
// recuadro del modo panel (se escala a 1220x686 sobre el video del grupo)
const Box: React.FC = () => (
	<AbsoluteFill style={{background: 'rgba(13,21,36,0.86)', borderRadius: 44, border: '3px solid rgba(255,255,255,0.16)',
		boxShadow: 'inset 0 0 0 1px rgba(0,0,0,0.3)'}} />
);

const Appear: React.FC<{at: number; children: React.ReactNode; style?: React.CSSProperties; dy?: number}> = ({at, children, style, dy = 24}) => {
	const p = useIn(at);
	return <div style={{opacity: p, transform: `translateY(${(1 - p) * dy}px)`, ...style}}>{children}</div>;
};

// ---------- portada / cierre ----------
const Title: React.FC<Props> = ({visual: v, dur}) => {
	const t = useT();
	const a = useIn(0.2, 0.8), b = useIn(0.7, 0.8), c = useIn(1.3, 0.8);
	const fadeOut = interpolate(t, [dur - 0.35, dur], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	const zoom = interpolate(t, [0, dur], [1.08, 1.18]);
	const panel = React.useContext(PanelCtx);
	if (panel) {
		return (
			<AbsoluteFill style={{fontFamily: FONT, color: C.white}}>
				<Box />
				<AbsoluteFill style={{opacity: fadeOut}}>
					<div style={{position: 'absolute', left: 110, top: 120, right: 110}}>
						<div style={{fontSize: 40, color: C.redSoft, fontWeight: 600, letterSpacing: 2, textTransform: 'uppercase', opacity: a}}>{v.kicker}</div>
						<div style={{fontSize: 128, fontWeight: 800, lineHeight: 1.02, marginTop: 20, letterSpacing: -2, opacity: a, transform: `translateY(${(1 - a) * 30}px)`}}>{v.title}</div>
						<div style={{width: 200, height: 10, background: C.red, borderRadius: 5, marginTop: 40, transform: `scaleX(${b})`, transformOrigin: 'left'}} />
						<div style={{marginTop: 40, fontSize: 44, lineHeight: 1.45, opacity: c, columnCount: 2, columnGap: 60}}>
							{v.members.map((m: string) => <div key={m}>{m}</div>)}
						</div>
						<div style={{marginTop: 34, fontSize: 30, color: C.muted, opacity: c}}>{v.footer}</div>
					</div>
				</AbsoluteFill>
			</AbsoluteFill>
		);
	}
	return (
		<AbsoluteFill style={{background: C.bg, fontFamily: FONT, color: C.white, opacity: fadeOut}}>
			<AbsoluteFill>
				<Img src={staticFile(v.bg)} style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(26px) brightness(0.32)', transform: `scale(${zoom})`}} />
			</AbsoluteFill>
			<AbsoluteFill style={{background: 'linear-gradient(90deg, rgba(13,21,36,0.92) 0%, rgba(13,21,36,0.55) 70%, rgba(13,21,36,0.2) 100%)'}} />
			<div style={{position: 'absolute', right: v.theme === 'mag' ? 110 : 150, top: v.theme === 'mag' ? 230 : 150,
				width: v.theme === 'mag' ? 760 : 420, height: v.theme === 'mag' ? 570 : 750, borderRadius: 24, overflow: 'hidden',
				boxShadow: '0 30px 80px rgba(0,0,0,0.5)', opacity: b, transform: `translateY(${(1 - b) * 30}px)`}}>
				<Img src={staticFile(v.bg)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
			</div>
			<div style={{position: 'absolute', left: 120, top: 220, width: v.theme === 'mag' ? 880 : 1150}}>
				<div style={{fontSize: 30, color: C.redSoft, fontWeight: 600, letterSpacing: 2, textTransform: 'uppercase', opacity: a}}>{v.kicker}</div>
				<div style={{fontSize: 96, fontWeight: 800, lineHeight: 1.04, marginTop: 18, letterSpacing: -1.5, opacity: a, transform: `translateY(${(1 - a) * 30}px)`}}>{v.title}</div>
				<div style={{width: 160, height: 8, background: C.red, borderRadius: 4, marginTop: 36, transform: `scaleX(${b})`, transformOrigin: 'left'}} />
				<div style={{marginTop: 40, fontSize: 32, lineHeight: 1.55, opacity: c}}>
					{v.members.map((m: string) => <div key={m}>{m}</div>)}
				</div>
				<div style={{marginTop: 34, fontSize: 22, color: C.muted, opacity: c}}>{v.footer}</div>
			</div>
		</AbsoluteFill>
	);
};

// ---------- viñetas ----------
const Bullets: React.FC<Props> = ({visual: v, dur, cues}) => (
	<Frame heading={v.heading} bg={v.bg} dur={dur}>
		{v.lead ? (
			<Appear at={cueAt(cues, v.lead.cue)} style={{fontSize: 38, lineHeight: 1.35, marginBottom: 40, maxWidth: 1500,
				borderLeft: `6px solid ${C.red}`, paddingLeft: 28}}>
				{v.lead.text}
			</Appear>
		) : null}
		<div style={{display: 'flex', gap: 60}}>
			<div style={{flex: 1}}>
				{v.items.map((it: any, i: number) => (
					<Appear key={i} at={cueAt(cues, it.cue, 0.5 + i)} style={{display: 'flex', alignItems: 'flex-start', gap: 26, marginBottom: 30}}>
						<div style={{minWidth: 52, height: 52, borderRadius: 26, background: C.red, display: 'flex', alignItems: 'center', justifyContent: 'center',
							fontSize: 26, fontWeight: 700}}>{i + 1}</div>
						<div style={{fontSize: 38, lineHeight: 1.3, paddingTop: 4}}>{it.text}</div>
					</Appear>
				))}
			</div>
			{v.eq ? (
				<Appear at={cueAt(cues, v.eq.cue)} style={{alignSelf: 'center'}}>
					<EqCard src={v.eq.src} h={110} />
				</Appear>
			) : null}
		</div>
	</Frame>
);


// ---------- chip de resultado (aparece con un pulso) ----------
const Chip: React.FC<{at: number; label?: string; value?: string; text?: string}> = ({at, label, value, text}) => {
	const f = useCurrentFrame();
	const {fps} = useVideoConfig();
	const p = spring({frame: f - Math.round(at * fps), fps, config: {damping: 12, stiffness: 160}});
	const glow = interpolate(f - Math.round(at * fps), [0, 10, 40], [0, 1, 0.35], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	return (
		<div style={{display: 'inline-flex', alignItems: 'center', gap: 18, padding: '14px 26px', borderRadius: 16, background: 'rgba(47,157,244,0.16)',
			border: `2px solid ${C.blue}`, boxShadow: `0 0 ${30 * glow}px rgba(47,157,244,${0.6 * glow})`, transform: `scale(${0.6 + 0.4 * p})`, opacity: p}}>
			{label ? <span style={{fontSize: 26, color: C.muted}}>{label}</span> : null}
			<span style={{fontSize: 34, fontWeight: 700, color: C.white, fontVariantNumeric: 'tabular-nums'}}>{value || text}</span>
		</div>
	);
};

// ---------- ecuaciones ----------
const EqCard: React.FC<{src: string; h: number; glow?: number}> = ({src, h, glow = 0}) => (
	<div style={{background: C.card, borderRadius: 16, padding: '18px 30px', display: 'inline-block',
		boxShadow: `0 10px 30px rgba(0,0,0,0.35), 0 0 0 ${glow * 5}px rgba(200,16,46,${0.55 * glow})`}}>
		<Img src={staticFile(src)} style={{height: h, maxWidth: 800, objectFit: 'contain', objectPosition: 'left', display: 'block'}} />
	</div>
);

const Equations: React.FC<Props> = ({visual: v, dur, cues}) => {
	const t = useT();
	const eqs = v.eqs as any[];
	const n = eqs.length;
	const cols = n > 4 ? 2 : 1;
	const h = eqs[0].big ? 200 : n > 4 ? 92 : n > 2 ? 104 : 150;
	const ats = eqs.map((e, i) => cueAt(cues, e.cue, 0.4 + i * 0.8) + (eqs.slice(0, i).filter((p) => p.cue === e.cue).length * 1.2));
	// la ecuación activa (la última que apareció) se resalta
	const active = ats.reduce((acc, a, i) => (t >= a ? i : acc), -1);
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'grid', gridTemplateColumns: `repeat(${cols}, 1fr)`, gridAutoFlow: cols === 2 ? 'column' : 'row',
				gridTemplateRows: cols === 2 ? `repeat(${Math.ceil(n / 2)}, auto)` : undefined, gap: '30px 40px', alignItems: 'start',
				justifyItems: eqs[0].big ? 'center' : 'start', marginTop: eqs[0].big ? 60 : 0}}>
				{eqs.map((e, i) => {
					const glow = active === i ? interpolate(t - ats[i], [0, 0.3], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
					return (
						<Appear key={i} at={ats[i]} dy={18}>
							<EqCard src={e.src} h={h} glow={n > 1 ? glow : 0} />
						</Appear>
					);
				})}
			</div>
			{v.counter ? (
				<div style={{position: 'absolute', bottom: 0, right: 0}}><Chip at={cueAt(cues, v.counter.cue)} label={v.counter.label} value={v.counter.value} text={v.counter.text} /></div>
			) : null}
			{v.note ? (
				<Appear at={cueAt(cues, v.note.cue)} style={{position: 'absolute', bottom: 0, left: 0, fontSize: 34, color: C.white,
					background: 'rgba(200,16,46,0.18)', border: `2px solid ${C.red}`, borderRadius: 14, padding: '14px 26px'}}>
					{v.note.text}
				</Appear>
			) : null}
		</Frame>
	);
};

// ---------- circuitos serie / paralelo con corriente animada ----------
const Resistor: React.FC<{x: number; y: number; vertical?: boolean; label: string}> = ({x, y, vertical, label}) => {
	const pts = [0, -14, 14, -14, 14, -14, 0].map((d, i) => (vertical ? `${x + d},${y - 60 + i * 20}` : `${x - 60 + i * 20},${y + d}`)).join(' ');
	return (
		<g>
			<polyline points={pts} fill="none" stroke={C.gold} strokeWidth={6} strokeLinejoin="round" />
			<text x={vertical ? (label.length > 3 ? x - 34 : x + 34) : x} y={vertical ? y + 10 : y - 34} fill={C.white} fontSize={30} fontWeight={700}
				textAnchor={vertical ? (label.length > 3 ? 'end' : 'start') : 'middle'} fontFamily={FONT}>{label}</text>
		</g>
	);
};
const Dots: React.FC<{d: string; len: number; speed: number; n: number}> = ({d, len, speed, n}) => {
	const t = useT();
	return (
		<path d={d} fill="none" stroke={C.redSoft} strokeWidth={9} strokeLinecap="round"
			strokeDasharray={`2 ${len / n - 2}`} strokeDashoffset={-t * speed} />
	);
};
const Circuit: React.FC<Props> = ({visual: v, dur, cues}) => {
	const serie = v.mode === 'serie';
	const draw = useIn(0.2, 1.2);
	const wire = {fill: 'none', stroke: C.wire, strokeWidth: 6};
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'flex', gap: 70, alignItems: 'flex-start'}}>
				<svg width={860} height={600} viewBox="0 0 860 600" style={{opacity: draw}}>
					{/* batería */}
					<line x1={80} y1={260} x2={80} y2={340} stroke={C.wire} strokeWidth={6} />
					<line x1={50} y1={285} x2={110} y2={285} stroke={C.white} strokeWidth={8} />
					<line x1={65} y1={315} x2={95} y2={315} stroke={C.white} strokeWidth={8} />
					<text x={20} y={250} fill={C.muted} fontSize={28} fontFamily={FONT}>10 V</text>
					{serie ? (
						<>
							<path d="M80 260 V80 H780 V520 H80 V340" {...wire} />
							<Dots d="M80 260 V80 H780 V520 H80 V340" len={2220} speed={160} n={22} />
							<rect x={170} y={60} width={140} height={40} fill={C.bg} />
							<rect x={460} y={60} width={140} height={40} fill={C.bg} />
							<rect x={760} y={230} width={40} height={140} fill={C.bg} />
							<Resistor x={240} y={80} label="R1 · 330 Ω" />
							<Resistor x={530} y={80} label="R2 · 330 Ω" />
							<Resistor x={780} y={300} vertical label="R3 · 560 Ω" />
						</>
					) : (
						<>
							<path d="M80 260 V80 H700 M80 340 V520 H700" {...wire} />
							{[300, 500, 700].map((x) => <path key={x} d={`M${x} 80 V520`} {...wire} />)}
							<Dots d="M80 260 V80 H700" len={800} speed={180} n={8} />
							<Dots d="M700 520 H80 V340" len={800} speed={180} n={8} />
							{[300, 500].map((x) => <Dots key={x} d={`M${x} 80 V520`} len={440} speed={120} n={5} />)}
							<Dots d="M700 80 V520" len={440} speed={70} n={5} />
							{[300, 500, 700].map((x) => <rect key={x} x={x - 20} y={230} width={40} height={140} fill={C.bg} />)}
							<Resistor x={300} y={300} vertical label="R1" />
							<Resistor x={500} y={300} vertical label="R2" />
							<Resistor x={700} y={300} vertical label="R3" />
						</>
					)}
				</svg>
				<div style={{flex: 1, paddingTop: 10}}>
					<Appear at={0.6}><EqCard src={v.eq} h={serie ? 70 : 90} /></Appear>
					<div style={{marginTop: 46}}>
						{v.facts.map((f: any, i: number) => (
							<Appear key={i} at={cueAt(cues, f.cue, 1 + i)} style={{fontSize: 34, lineHeight: 1.3, marginBottom: 26, display: 'flex', gap: 18}}>
								<span style={{color: C.redSoft, fontWeight: 800}}>▸</span><span>{f.text}</span>
							</Appear>
						))}
					</div>
				</div>
			</div>
		</Frame>
	);
};

// ---------- multímetro ----------
const Meter: React.FC<{kind: number}> = ({kind}) => {
	const sym = ['Ω', 'V', 'A'][kind];
	return (
		<svg width={150} height={150} viewBox="0 0 150 150">
			<rect x={25} y={10} width={100} height={130} rx={16} fill={C.gold} />
			<rect x={38} y={24} width={74} height={34} rx={5} fill="#cfe3c8" />
			<circle cx={75} cy={95} r={26} fill="#222" />
			<text x={75} y={106} fill={C.white} fontSize={30} fontWeight={800} textAnchor="middle" fontFamily={FONT}>{sym}</text>
		</svg>
	);
};
const Measure: React.FC<Props> = ({visual: v, dur, cues}) => (
	<Frame heading={v.heading} dur={dur}>
		<div style={{display: 'flex', alignItems: 'center', gap: 50}}>
			<Appear at={0.4}><EqCard src={v.eq} h={95} /></Appear>
			<Appear at={2.0} style={{fontSize: 34, lineHeight: 1.35, maxWidth: 700}}>
				Banda dorada = ±5 %: el valor real puede diferir del nominal dentro de ese margen.
			</Appear>
		</div>
		<div style={{display: 'flex', gap: 40, marginTop: 70}}>
			{v.cards.map((c: any, i: number) => (
				<Appear key={i} at={cueAt(cues, c.cue, 3 + i)} style={{flex: 1, background: 'rgba(255,255,255,0.06)', border: '1px solid rgba(255,255,255,0.14)',
					borderRadius: 22, padding: '26px 30px', display: 'flex', alignItems: 'center', gap: 22}}>
					<Meter kind={i} />
					<div>
						<div style={{fontSize: 36, fontWeight: 700, color: C.redSoft}}>{c.title}</div>
						<div style={{fontSize: 30, lineHeight: 1.3, marginTop: 8}}>{c.text}</div>
					</div>
				</Appear>
			))}
		</div>
	</Frame>
);

// ---------- tablas ----------
const Table: React.FC<Props> = ({visual: v, dur, cues}) => {
	const t = useT();
	const marks = (v.marks as any[]).map((m) => ({...m, at: cueAt(cues, m.cue)}));
	const on = (r: number, c: number) => marks.some((m) => t >= m.at && m.col === c && (m.row === undefined || m.row === r));
	return (
		<Frame heading={v.heading} dur={dur}>
			<Appear at={0.3}>
				<table style={{borderCollapse: 'separate', borderSpacing: 0, width: '100%', fontSize: 38, background: 'rgba(255,255,255,0.04)',
					borderRadius: 18, overflow: 'hidden'}}>
					<thead>
						<tr>{v.cols.map((c: string, i: number) => (
							<th key={i} style={{background: C.red, padding: '22px 26px', textAlign: i ? 'center' : 'left', fontWeight: 700, fontSize: 32}}>{c}</th>
						))}</tr>
					</thead>
					<tbody>
						{v.rows.map((r: string[], ri: number) => (
							<tr key={ri} style={{background: ri % 2 ? 'rgba(255,255,255,0.05)' : 'transparent', fontWeight: ri === v.rows.length - 1 && v.rows.length > 3 ? 700 : 400}}>
								{r.map((cell, ci) => {
									const hl = on(ri, ci);
									return (
										<td key={ci} style={{padding: '22px 26px', textAlign: ci ? 'center' : 'left', borderTop: '1px solid rgba(255,255,255,0.08)',
											color: hl ? C.ink : C.white, background: hl ? C.gold : 'transparent', fontVariantNumeric: 'tabular-nums'}}>{cell}</td>
									);
								})}
							</tr>
						))}
					</tbody>
				</table>
			</Appear>
			<div style={{display: 'flex', gap: 30, alignItems: 'center', marginTop: 28}}>
				{(v.eqs || []).map((e: any, i: number) => <Appear key={i} at={cueAt(cues, e.cue)}><EqCard src={e.src} h={74} /></Appear>)}
				{v.counter ? <Chip at={cueAt(cues, v.counter.cue)} label={v.counter.label} value={v.counter.value} text={v.counter.text} /> : null}
			</div>
		</Frame>
	);
};

// ---------- bombillas ----------
const Bulb: React.FC<{x: number; y: number; level: number; label: string}> = ({x, y, level, label}) => {
	const t = useT();
	const flick = 1 + 0.03 * Math.sin(t * 9 + x);
	const g = level * flick;
	return (
		<g>
			<circle cx={x} cy={y} r={70 * (0.6 + g)} fill={`rgba(255,214,90,${0.35 * g})`} />
			<circle cx={x} cy={y} r={36} fill={`rgb(${120 + 135 * g},${110 + 110 * g},${60 + 40 * g})`} stroke={C.white} strokeWidth={4} />
			<path d={`M${x - 14} ${y + 8} q7 -22 14 0 q7 22 14 0`} fill="none" stroke="#5a3b00" strokeWidth={3} />
			<text x={x} y={y + 78} fill={C.white} fontSize={30} fontWeight={700} textAnchor="middle" fontFamily={FONT}>{label}</text>
		</g>
	);
};
const Bulbs: React.FC<Props> = ({visual: v, dur, cues}) => {
	const on = useIn(1.2, 1.0); // se cierra el interruptor y encienden
	const wire = {fill: 'none', stroke: C.wire, strokeWidth: 6};
	let body: React.ReactNode;
	if (v.fig === 'a') {
		body = (<>
			<path d="M120 300 V120 H740 V480 H120 V360" {...wire} />
			<rect x={280} y={100} width={80} height={40} fill={C.bg} /><rect x={520} y={100} width={80} height={40} fill={C.bg} />
			<Bulb x={320} y={120} level={0.25 * on} label="L1 · V/2" />
			<Bulb x={560} y={120} level={0.25 * on} label="L2 · V/2" />
		</>);
	} else if (v.fig === 'b') {
		body = (<>
			<path d="M120 300 V120 H640 V480 H120 V360 M380 120 V480" {...wire} />
			<rect x={360} y={260} width={40} height={80} fill={C.bg} /><rect x={620} y={260} width={40} height={80} fill={C.bg} />
			<Bulb x={380} y={300} level={1 * on} label="L1 · V" />
			<Bulb x={640} y={300} level={1 * on} label="L2 · V" />
		</>);
	} else {
		body = (<>
			<path d="M120 300 V120 H500 M500 120 V60 H760 V120 M500 120 V180 H760 V120 M760 120 H800 V480 H120 V360" {...wire} />
			<rect x={260} y={100} width={80} height={40} fill={C.bg} /><rect x={590} y={40} width={80} height={40} fill={C.bg} /><rect x={590} y={160} width={80} height={40} fill={C.bg} />
			<Bulb x={300} y={120} level={0.45 * on} label="L1 · 2V/3" />
			<g transform="translate(0,0)">
				<Bulb x={630} y={60} level={0.11 * on} label="" />
				<Bulb x={630} y={180} level={0.11 * on} label="" />
			</g>
			<text x={830} y={70} fill={C.white} fontSize={28} fontWeight={700} fontFamily={FONT}>L2 · V/3</text>
			<text x={830} y={190} fill={C.white} fontSize={28} fontWeight={700} fontFamily={FONT}>L3 · V/3</text>
		</>);
	}
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'flex', gap: 50}}>
				<svg width={1020} height={560} viewBox="0 0 1020 560">
					<line x1={120} y1={300} x2={120} y2={360} stroke={C.wire} strokeWidth={6} />
					<line x1={90} y1={320} x2={150} y2={320} stroke={C.white} strokeWidth={8} />
					<line x1={105} y1={344} x2={135} y2={344} stroke={C.white} strokeWidth={8} />
					<text x={40} y={410} fill={C.muted} fontSize={28} fontFamily={FONT}>V</text>
					{body}
				</svg>
				<div style={{flex: 1, paddingTop: 30}}>
					{v.facts.map((f: any, i: number) => (
						<Appear key={i} at={cueAt(cues, f.cue, 1 + i)} style={{fontSize: 34, lineHeight: 1.3, marginBottom: 30, display: 'flex', gap: 18}}>
							<span style={{color: C.gold, fontWeight: 800}}>▸</span><span>{f.text}</span>
						</Appear>
					))}
				</div>
			</div>
		</Frame>
	);
};

// ---------- figura (gráfica del informe): se revela de izquierda a derecha ----------
const Figure: React.FC<Props> = ({visual: v, dur, cues}) => {
	const panel = React.useContext(PanelCtx);
	const f = useCurrentFrame();
	const {fps} = useVideoConfig();
	const facts = (v.facts || []) as any[];
	const rev = v.reveal ? interpolate(f, [Math.round(0.3 * fps), Math.round(1.8 * fps)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.cubic)}) : 1;
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'flex', gap: 40, alignItems: 'flex-start', height: '100%'}}>
				<Appear at={0.2} style={{flex: facts.length ? 2.1 : 1, background: C.card, borderRadius: 18, padding: 16, position: 'relative',
					boxShadow: '0 10px 30px rgba(0,0,0,0.35)', display: 'flex', flexDirection: 'column'}}>
					<div style={{clipPath: `inset(0 ${(1 - rev) * 100}% 0 0)`}}>
						<Img src={staticFile(v.src)} style={{width: '100%', maxHeight: panel ? 600 : 640, objectFit: 'contain', display: 'block'}} />
					</div>
					{rev < 1 ? <div style={{position: 'absolute', top: 16, bottom: 16, left: `calc(16px + ${rev * 100}% * (1 - 32px / 100%))`, width: 4, background: C.blue, boxShadow: `0 0 18px ${C.blue}`}} /> : null}
					{v.caption ? <div style={{color: C.ink, fontSize: 24, marginTop: 10, textAlign: 'center'}}>{v.caption}</div> : null}
				</Appear>
				{facts.length ? (
					<div style={{flex: 1, paddingTop: 6}}>
						{facts.map((fc: any, i: number) => (
							<Appear key={i} at={cueAt(cues, fc.cue, 1 + i)} style={{fontSize: 31, lineHeight: 1.3, marginBottom: 22, display: 'flex', gap: 16}}>
								<span style={{color: C.blue, fontWeight: 800}}>▸</span><span>{fc.text}</span>
							</Appear>
						))}
						{v.eq ? <Appear at={cueAt(cues, v.eqcue, 2)}><EqCard src={v.eq} h={78} /></Appear> : null}
					</div>
				) : null}
			</div>
		</Frame>
	);
};

// ---------- utilidades SVG animadas ----------
// trazo que se dibuja solo (pathLength=1 normaliza el largo)
const Draw: React.FC<{d: string; at: number; dur?: number; stroke: string; width: number; dash?: boolean}> = ({d, at, dur = 1.2, stroke, width, dash}) => {
	const f = useCurrentFrame();
	const {fps} = useVideoConfig();
	const p = interpolate(f, [Math.round(at * fps), Math.round((at + dur) * fps)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
	return <path d={d} fill="none" stroke={stroke} strokeWidth={width} strokeLinecap="round" pathLength={1}
		strokeDasharray={dash ? '0.02 0.012' : '1'} strokeDashoffset={dash ? 0 : 1 - p} opacity={dash ? p : 1} />;
};
// puntos de corriente recorriendo un camino
const Flow: React.FC<{d: string; speed?: number; n?: number; color?: string; width?: number}> = ({d, speed = 0.35, n = 14, color = C.redSoft, width = 8}) => {
	const t = useT();
	return <path d={d} fill="none" stroke={color} strokeWidth={width} strokeLinecap="round" pathLength={1}
		strokeDasharray={`0.012 ${1 / n - 0.012}`} strokeDashoffset={-t * speed} />;
};
const relB = (x: number, R: number) => Math.pow(R, 3) / Math.pow(x * x + R * R, 1.5); // B(x)/B(0) de una espira

// ---------- bobina: corriente circulando y campo sobre el eje ----------
const Coil: React.FC<Props> = ({visual: v, dur, cues}) => {
	const t = useT();
	const draw = useIn(0.2, 1.0);
	const cx = 170, cy = 360, R = 125, rx = 34, ry = R; // elipse en perspectiva
	const ring = `M${cx} ${cy - ry} a${rx} ${ry} 0 1 0 0.01 0`;
	const xs = Array.from({length: 11}, (_, i) => i * 64);
	const prof = xs.map((x, i) => `${i ? 'L' : 'M'}${cx + x} ${cy - 30 - 230 * relB(x, R)}`).join(' ');
	const sx = (t * 70) % 640; // sensor que recorre el eje
	const sB = relB(sx, R);
	const eqAt = cueAt(cues, v.eqcue, 6);
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'flex', gap: 30, alignItems: 'flex-start'}}>
				<svg width={880} height={640} viewBox="0 0 880 640" style={{opacity: draw}}>
					<line x1={cx} y1={cy} x2={850} y2={cy} stroke={C.wire} strokeWidth={3} strokeDasharray="8 8" />
					<text x={840} y={cy + 36} fill={C.muted} fontSize={26} textAnchor="end" fontFamily={FONT}>eje x</text>
					{/* campo en el eje: flechas cuya longitud sigue B(x) */}
					{xs.map((x, i) => {
						const L = 54 * relB(x, R);
						return (
							<g key={i} opacity={interpolate(t, [0.6 + i * 0.12, 1.1 + i * 0.12], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}>
								<line x1={cx + x - L / 2} y1={cy} x2={cx + x + L / 2} y2={cy} stroke={C.blue} strokeWidth={6} strokeLinecap="round" />
								<polygon points={`${cx + x + L / 2 + 8},${cy} ${cx + x + L / 2 - 6},${cy - 7} ${cx + x + L / 2 - 6},${cy + 7}`} fill={C.blue} />
							</g>
						);
					})}
					<Draw d={prof} at={1.0} dur={1.6} stroke={C.blue} width={5} />
					<text x={cx + 260} y={cy - 262} fill={C.blue} fontSize={28} fontFamily={FONT} fontWeight={700}>B(x) sobre el eje</text>
					{/* bobina con corriente */}
					<path d={ring} fill="rgba(47,157,244,0.08)" stroke={C.gold} strokeWidth={10} />
					<Flow d={ring} />
					<text x={cx} y={cy + ry + 44} fill={C.white} fontSize={28} fontWeight={700} textAnchor="middle" fontFamily={FONT}>N espiras · radio R</text>
					<text x={cx - rx - 14} y={cy + 8} fill={C.gold} fontSize={28} fontWeight={800} textAnchor="end" fontFamily={FONT}>I</text>
					{/* sensor que se desplaza */}
					<g transform={`translate(${cx + sx}, ${cy})`}>
						<rect x={-14} y={-30} width={28} height={60} rx={6} fill={C.blue} stroke={C.white} strokeWidth={3} />
						<text x={0} y={92} fill={C.white} fontSize={28} textAnchor="middle" fontFamily={FONT}>B = {sB.toFixed(2).replace('.', ',')} B₀</text>
					</g>
				</svg>
				<div style={{flex: 1}}>
					{v.facts.map((fc: any, i: number) => (
						<Appear key={i} at={cueAt(cues, fc.cue, 1 + i)} style={{fontSize: 31, lineHeight: 1.3, marginBottom: 22, display: 'flex', gap: 16}}>
							<span style={{color: C.blue, fontWeight: 800}}>▸</span><span>{fc.text}</span>
						</Appear>
					))}
					<Appear at={eqAt}><EqCard src={v.eq} h={110} glow={interpolate(t - eqAt, [0, 0.4], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})} /></Appear>
				</div>
			</div>
		</Frame>
	);
};

// ---------- par de Helmholtz: dos bobinas y la meseta de campo ----------
const Helmholtz: React.FC<Props> = ({visual: v, dur, cues}) => {
	const t = useT();
	const draw = useIn(0.2, 1.0);
	const pairAt = cueAt(cues, v.pairCue, 6);
	const R = 120, ax = 200, ay = 120, mid = 470; // bobinas en mid ± R/2
	const X = (u: number) => mid + u * R;          // u en unidades de R
	const Y = (b: number) => 600 - 270 * b / 1.5;   // b relativo a B(0) de una bobina
	const us = Array.from({length: 121}, (_, i) => -3 + i * 0.05);
	const one = us.map((u, i) => `${i ? 'L' : 'M'}${X(u)} ${Y(relB(u, 1))}`).join(' ');
	const pair = us.map((u, i) => `${i ? 'L' : 'M'}${X(u)} ${Y(relB(u - 0.5, 1) + relB(u + 0.5, 1))}`).join(' ');
	const ring = (x: number) => `M${x} ${ay - 70} a18 70 0 1 0 0.01 0`;
	const pulse = 0.5 + 0.5 * Math.sin(t * 3);
	const show2 = t >= pairAt;
	return (
		<Frame heading={v.heading} dur={dur}>
			<div style={{display: 'flex', gap: 30, alignItems: 'flex-start'}}>
				<svg width={900} height={640} viewBox="0 0 900 640" style={{opacity: draw}}>
					<line x1={100} y1={ay} x2={860} y2={ay} stroke={C.wire} strokeWidth={3} strokeDasharray="8 8" />
					<text x={850} y={ay + 34} fill={C.muted} fontSize={24} textAnchor="end" fontFamily={FONT}>eje</text>
					{/* región entre las bobinas */}
					<rect x={X(-0.5)} y={Y(1.75)} width={R} height={Y(0) - Y(1.75)} fill={C.blue} opacity={show2 ? 0.12 + 0.08 * pulse : 0} />
					{/* bobinas */}
					<g opacity={1}><path d={ring(X(show2 ? -0.5 : 0))} fill="none" stroke={C.gold} strokeWidth={9} /><Flow d={ring(X(show2 ? -0.5 : 0))} n={10} /></g>
					<g opacity={show2 ? 1 : 0}><path d={ring(X(0.5))} fill="none" stroke={C.gold} strokeWidth={9} /><Flow d={ring(X(0.5))} n={10} /></g>
					{show2 ? <>
						<line x1={X(-0.5)} y1={ay - 90} x2={X(0.5)} y2={ay - 90} stroke={C.white} strokeWidth={3} />
						<text x={mid} y={ay - 102} fill={C.white} fontSize={26} textAnchor="middle" fontFamily={FONT}>separación = R</text>
					</> : null}
					{/* perfiles */}
					<line x1={100} y1={Y(0)} x2={860} y2={Y(0)} stroke={C.wire} strokeWidth={2} />
					<Draw d={one} at={0.8} dur={1.4} stroke={C.white} width={4} dash />
					<text x={X(-2.95)} y={Y(relB(2.2, 1)) - 14} fill={C.muted} fontSize={24} fontFamily={FONT}>una bobina</text>
					{show2 ? <>
						<Draw d={pair} at={pairAt + 0.2} dur={1.6} stroke={C.blue} width={6} />
						<text x={X(0.75)} y={Y(1.431) - 16} fill={C.blue} fontSize={26} fontWeight={700} fontFamily={FONT}>par de Helmholtz: meseta, 1,43 × B(0)</text>
					</> : null}
					<text x={X(0)} y={Y(0) + 32} fill={C.muted} fontSize={24} textAnchor="middle" fontFamily={FONT}>posición sobre el eje</text>
				</svg>
				<div style={{flex: 1, display: 'flex', flexDirection: 'column', gap: 22}}>
					{v.eqs.map((e: any, i: number) => <Appear key={i} at={cueAt(cues, e.cue, 1 + i * 2)}><EqCard src={e.src} h={i === 1 ? 104 : 84} /></Appear>)}
				</div>
			</div>
		</Frame>
	);
};

const KINDS: Record<string, React.FC<Props>> = {figure: Figure, coil: Coil, helmholtz: Helmholtz, title: Title, bullets: Bullets, equations: Equations, circuit: Circuit, measure: Measure, table: Table, bulbs: Bulbs};
const Slide: React.FC<Props> = (p) => {
	const K = KINDS[p.visual.kind];
	return <BrandCtx.Provider value={p.brand || 'Experiencia 4 · Circuitos resistivos y ley de Ohm'}><PanelCtx.Provider value={!!p.panel}><K {...p} /></PanelCtx.Provider></BrandCtx.Provider>;
};

export const Root: React.FC = () => (
	<Composition id="Slide" component={Slide as any} fps={30} width={1920} height={1080} durationInFrames={150}
		defaultProps={{visual: {kind: 'title', bg: 'img/grupo.jpg', title: 'Prueba', kicker: '', members: [], footer: ''}, dur: 5, cues: {}}}
		calculateMetadata={({props}: any) => ({durationInFrames: Math.round(props.dur * 30)})} />
);

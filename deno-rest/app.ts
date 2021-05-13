import { Application, Router, Status } from "https://deno.land/x/oak@v6.5.0/mod.ts";

const app = new Application();
const router = new Router();

router.get("/fibonacci/v1/sequence/:order", (ctx: any) => {
    const order = parseInt(ctx.params.order);
    const f = [0, 1];
    for (let i = 2, l = order; i <= l; i++) {
        f.push(f[i - 1] + f[i - 2]);
    }
    ctx.response.status = Status.OK;
    ctx.response.type = "json";
    ctx.response.body =  {
        data: {
            value: f[order]
        }
    };
});

app.use(router.routes());

console.log("app running -> http://localhost:3000");
await app.listen({ port: 3000 });
